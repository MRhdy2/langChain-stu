"""Track token usage reported by the configured DeepSeek chat model."""

import threading
from typing import Any, Dict, List

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class GenericLLMsCallbackHandler(BaseCallbackHandler):
    """Collect request and token counts without estimating provider prices."""

    total_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    successful_requests: int = 0

    def __init__(self) -> None:
        super().__init__()
        self._lock = threading.Lock()

    def __repr__(self) -> str:
        return (
            f"Tokens Used: {self.total_tokens}\n"
            f"\tPrompt Tokens: {self.prompt_tokens}\n"
            f"\tCompletion Tokens: {self.completion_tokens}\n"
            f"Successful Requests: {self.successful_requests}"
        )

    @property
    def always_verbose(self) -> bool:
        return True

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        token_usage = (response.llm_output or {}).get("token_usage") or {}
        if not token_usage and response.generations and response.generations[-1]:
            generation_info = response.generations[-1][-1].generation_info or {}
            token_usage = generation_info.get("token_usage") or {}

        prompt_tokens = token_usage.get("prompt_tokens", token_usage.get("input_tokens", 0))
        completion_tokens = token_usage.get(
            "completion_tokens", token_usage.get("output_tokens", 0)
        )
        total_tokens = token_usage.get("total_tokens", prompt_tokens + completion_tokens)

        with self._lock:
            self.prompt_tokens += prompt_tokens
            self.completion_tokens += completion_tokens
            self.total_tokens += total_tokens
            self.successful_requests += 1

    def __copy__(self) -> "GenericLLMsCallbackHandler":
        return self

    def __deepcopy__(self, memo: Any) -> "GenericLLMsCallbackHandler":
        return self

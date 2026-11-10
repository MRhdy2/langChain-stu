from __future__ import annotations

import logging
from contextlib import contextmanager
from contextvars import ContextVar
from typing import (
    Generator,
    Optional,
)

from langchain_core.tracers.context import register_configure_hook

from .generic_llms_info import GenericLLMsCallbackHandler

logger = logging.getLogger(__name__)

generic_llms_callback_var: ContextVar[Optional[GenericLLMsCallbackHandler]] = ContextVar(
    "generic_llms_callback", default=None
)

register_configure_hook(generic_llms_callback_var, True)


@contextmanager
def get_generic_llms_callback() -> Generator[GenericLLMsCallbackHandler, None, None]:
    """Get the model callback handler in a context manager.
    It exposes request and token counts reported by DeepSeek.

    Returns:
        GenericLLMsCallbackHandler: The Generic callback handler.

    Example:
        >>> with get_generic_llms_callback() as cb:
        ...     # Call the DeepSeek model here
    """
    cb = GenericLLMsCallbackHandler()
    generic_llms_callback_var.set(cb)
    yield cb
    generic_llms_callback_var.set(None)

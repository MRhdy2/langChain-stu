"""DeepSeek chat models and local embeddings for the tutorial notebooks."""

import os
import sys
from pathlib import Path

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_openai import ChatOpenAI
from openai import OpenAI


DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-flash"
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"
KEY_FILE = Path(sys.prefix) / "share" / "langchain_tutorial" / "deepseek_api_key"


def _api_key() -> str:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key and KEY_FILE.is_file():
        key = KEY_FILE.read_text(encoding="utf-8").strip()
    if not key:
        raise RuntimeError("请设置环境变量 DEEPSEEK_API_KEY，或配置环境内的 deepseek_api_key 文件")
    return key


def get_deepseek_chat(**kwargs) -> ChatOpenAI:
    """Return a LangChain chat model configured for DeepSeek.

    Non-thinking mode keeps tool-call conversations compatible with the
    LangChain version used by these notebooks.
    """
    return ChatOpenAI(
        model_name=os.environ.get("DEEPSEEK_MODEL", DEFAULT_MODEL),
        openai_api_key=_api_key(),
        openai_api_base=DEEPSEEK_BASE_URL,
        model_kwargs={"extra_body": {"thinking": {"type": "disabled"}}},
        **kwargs,
    )


def get_deepseek_client() -> OpenAI:
    """Return the OpenAI-compatible SDK client for direct API examples."""
    return OpenAI(api_key=_api_key(), base_url=DEEPSEEK_BASE_URL)


def get_local_embeddings() -> FastEmbedEmbeddings:
    """Run Chinese text embeddings locally; no second API key is needed."""
    cache_dir = Path(sys.prefix) / "share" / "fastembed"
    return FastEmbedEmbeddings(
        model_name=EMBEDDING_MODEL,
        cache_dir=str(cache_dir),
    )

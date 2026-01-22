from openai import AsyncOpenAI
from pydantic import Field
from pydantic_settings import BaseSettings

AsyncOpenAI()


class OpenAIEmbedderConfig(BaseSettings):
    """OpenAI-compatible embedder settings."""

    base_url: str = Field(alias="VDB_MCP_OPENAI_BASE_URL")
    api_key: str = Field( alias="VDB_MCP_OPENAI_API_KEY")
    model: str = Field(alias="VDB_MCP_OPENAI_MODEL")
    timeout: float = Field(
        default=30,
        alias="VDB_MCP_OPENAI_TIMEOUT",
    )
    max_retries: int = Field(
        default=3,
        gt=0,
        alias="VDB_MCP_OPENAI_MAX_RETRIES",
    )

from pydantic import Field
from pydantic_settings import BaseSettings


class FastembedEmbedderConfig(BaseSettings):
    """Fastembed embedder settings."""

    model_name: str = Field(alias="VDB_MCP_FASTEMBED_MODEL_NAME")
    cache_dir: str | None = Field(
        default=None,
        alias="VDB_MCP_FASTEMBED_CACHE_DIR",
    )
    threads: int = Field(
        default=1,
        alias="VDB_MCP_FASTEMBED_THREADS",
    )

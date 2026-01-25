from pydantic import Field
from pydantic_settings import BaseSettings


class QdrantConfig(BaseSettings):
    """Qdrant settings."""

    host: str = Field(alias="VDB_MCP_QDRANT_HOST")
    port: int = Field(alias="VDB_MCP_QDRANT_PORT")
    grpc_port: int = Field(alias="VDB_MCP_QDRANT_GRPC_PORT")
    prefer_grpc: bool = Field(
        default=True,
        alias="VDB_MCP_QDRANT_PREFER_GRPC",
    )
    api_key: str | None = Field(
        default=None,
        alias="VDB_MCP_QDRANT_PREFER_GRPC",
    )

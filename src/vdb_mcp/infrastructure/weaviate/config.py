from pydantic import Field
from pydantic_settings import BaseSettings


class WeaviateConfig(BaseSettings):
    """Weaviate settings."""

    http_host: str = Field(
        default="localhost",
        alias="VDB_MCP_WEAVIATE_HTTP_HOST",
    )
    http_port: int = Field(
        default=8080,
        alias="VDB_MCP_WEAVIATE_HTTP_PORT",
    )
    http_secure: bool = Field(
        default=False,
        alias="VDB_MCP_WEAVIATE_HTTP_SECURE",
    )
    grpc_host: str = Field(
        default="localhost",
        alias="VDB_MCP_WEAVIATE_GRPC_HOST",
    )
    grpc_port: int = Field(
        default=50051,
        alias="VDB_MCP_WEAVIATE_GRPC_PORT",
    )
    grpc_secure: bool = Field(
        default=False,
        alias="VDB_MCP_WEAVIATE_GRPC_SECURE",
    )
    api_key: str | None = Field(
        default=None,
        alias="VDB_MCP_WEAVIATE_API_KEY",
    )

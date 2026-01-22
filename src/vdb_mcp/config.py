from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class VDBMCPConfig(BaseSettings):
    """VDB MCP config."""

    embeddings_provider: Literal["fastembed", "openai"] = Field(
        alias="VDB_MCP_EMBEDDINGS_PROVIDER",
    )
    vector_store_provider: Literal["weaviate", "qdrant"] = Field(
        alias="VDB_MCP_VECTOR_STORE_PROVIDER",
    )

    create_collection_tool_description: str = Field(
        default="",
        alias="VDB_MCP_CREATE_COLLECTION_TOOL_DESCRIPTION",
    )
    delete_collection_tool_description: str = Field(
        default="",
        alias="VDB_MCP_DELETE_COLLECTION_TOOL_DESCRIPTION",
    )
    insert_one_tool_description: str = Field(
        default="",
        alias="VDB_MCP_INSERT_ONE_TOOL_DESCRIPTION",
    )
    search_tool_description: str = Field(
        default="",
        alias="VDB_MCP_SEARCH_TOOL_DESCRIPTION",
    )

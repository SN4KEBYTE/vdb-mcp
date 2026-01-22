from dishka import AsyncContainer
from mcp.server import FastMCP

from vdb_mcp.config import VDBMCPConfig
from vdb_mcp.presentation.mcp.tools import (
    create_collection,
    delete_collection,
    insert_one,
    search,
)


def create_mcp_server(
    container: AsyncContainer,
    config: VDBMCPConfig,
) -> FastMCP:
    """Create FastMCP server."""
    # TODO: lifespan with dishka container close
    mcp = FastMCP(name="vdb-mcp-server")
    mcp.di_container = container
    mcp.add_tool(
        create_collection,
        name="vector-store-create-collection",
        description=config.create_collection_tool_description,
    )
    mcp.add_tool(
        delete_collection,
        name="vector-store-delete-collection",
        description=config.delete_collection_tool_description,
    )
    mcp.add_tool(
        insert_one,
        name="vector-store-insert-one",
        description=config.insert_one_tool_description,
    )
    mcp.add_tool(
        search,
        name="vector-store-search",
        description=config.search_tool_description,
    )

    return mcp

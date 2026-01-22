import uvloop

from dishka import make_async_container

from vdb_mcp.config import VDBMCPConfig
from vdb_mcp.infrastructure.utils import get_embeddings_provider, get_vector_store_provider
from vdb_mcp.presentation.mcp.app import create_mcp_server


async def main() -> None:
    """Application entrypoint."""
    config = VDBMCPConfig()
    container = make_async_container(
        get_embeddings_provider(config),
        get_vector_store_provider(config),
    )
    mcp = create_mcp_server(
        container,
        config,
    )
    mcp.run()


if __name__ == "__main__":
    uvloop.run(main())

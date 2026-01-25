from typing import AsyncIterable

from dishka import Provider, Scope, provide
from qdrant_client import AsyncQdrantClient

from vdb_mcp.infrastructure.qdrant.config import QdrantConfig
from vdb_mcp.infrastructure.qdrant.vector_store import QdrantVectorStore


class QdrantVectorStoreProvider(Provider):
    """Dependency provider for Qdrant vector store."""

    @provide(scope=Scope.APP)
    def qdrant_config(
        self,
    ) -> QdrantConfig:
        """Get Qdrant config."""
        return QdrantConfig()

    @provide(scope=Scope.APP)
    async def qdrant_client(
        self,
        qdrant_config: QdrantConfig,
    ) -> AsyncIterable[AsyncQdrantClient]:
        """Get Qdrant client."""
        client = AsyncQdrantClient(
            url=qdrant_config.host,
            port=qdrant_config.port,
            grpc_port=qdrant_config.grpc_port,
            prefer_grpc=qdrant_config.prefer_grpc,
            api_key=qdrant_config.api_key,
        )

        try:
            yield client
        finally:
            await client.close()

    @provide(scope=Scope.APP)
    def qdrant_vector_store(
        self,
        qdrant_client: AsyncQdrantClient,
    ) -> QdrantVectorStore:
        """Get Qdrant vector store."""
        return QdrantVectorStore(qdrant_client)

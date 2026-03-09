from typing import AsyncIterable

from dishka import Provider, Scope, provide
from weaviate import WeaviateAsyncClient
from weaviate.auth import AuthApiKey
from weaviate.connect import ConnectionParams

from vdb_mcp.application.ports.vector_store import VectorStore
from vdb_mcp.infrastructure.weaviate.config import WeaviateConfig
from vdb_mcp.infrastructure.weaviate.vector_store import WeaviateVectorStore


class WeaviateVectorStoreProvider(Provider):
    """Dependency provider for Weaviate vector store."""

    @provide(scope=Scope.APP)
    def weaviate_config(
        self,
    ) -> WeaviateConfig:
        """Get Weaviate config."""
        return WeaviateConfig()

    @provide(scope=Scope.APP)
    async def weaviate_client(
        self,
        weaviate_config: WeaviateConfig,
    ) -> AsyncIterable[WeaviateAsyncClient]:
        """Get Weaviate async client."""
        auth_credentials = None

        if weaviate_config.api_key is not None:
            auth_credentials = AuthApiKey(weaviate_config.api_key)

        client = WeaviateAsyncClient(
            connection_params=ConnectionParams.from_params(
                http_host=weaviate_config.http_host,
                http_port=weaviate_config.http_port,
                http_secure=weaviate_config.http_secure,
                grpc_host=weaviate_config.grpc_host,
                grpc_port=weaviate_config.grpc_port,
                grpc_secure=weaviate_config.grpc_secure,
            ),
            auth_client_secret=auth_credentials,
        )

        await client.connect()

        try:
            yield client
        finally:
            await client.close()

    @provide(scope=Scope.APP)
    def weaviate_vector_store(
        self,
        weaviate_client: WeaviateAsyncClient,
    ) -> VectorStore:
        """Get Weaviate vector store."""
        return WeaviateVectorStore(weaviate_client)

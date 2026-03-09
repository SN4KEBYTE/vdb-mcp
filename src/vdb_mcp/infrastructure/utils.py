from types import MappingProxyType

from dishka import Provider

from vdb_mcp.config import VDBMCPConfig
from vdb_mcp.infrastructure.fast_embed.di_provider import FastembedEmbedderProvider
from vdb_mcp.infrastructure.open_ai.di_provider import OpenAIEmbedderProvider
from vdb_mcp.infrastructure.qdrant.di_provider import QdrantVectorStoreProvider
from vdb_mcp.infrastructure.weaviate.di_provider import WeaviateVectorStoreProvider

_EMBEDDINGS_PROVIDERS = MappingProxyType(
    {
        "fastembed": FastembedEmbedderProvider,
        "openai": OpenAIEmbedderProvider,
    },
)
_VECTOR_STORE_PROVIDERS = MappingProxyType(
    {
        "weaviate": WeaviateVectorStoreProvider,
        "qdrant": QdrantVectorStoreProvider,
    },
)


def get_embeddings_provider(
    config: VDBMCPConfig,
) -> Provider:
    provider = config.embeddings_provider
    provider_cls = _EMBEDDINGS_PROVIDERS.get(provider)

    if provider_cls is None:
        raise ValueError(
            f"unknown embeddings provider {provider}, use 'openai' or 'fastembed'"
        )

    return provider_cls()


def get_vector_store_provider(
    config: VDBMCPConfig,
) -> Provider:
    provider = config.vector_store_provider
    provider_cls = _VECTOR_STORE_PROVIDERS.get(provider)

    if provider_cls is None:
        raise ValueError(
            f"unknown vector store provider {provider}, use 'qdrant' or 'weaviate'"
        )

    return provider_cls()

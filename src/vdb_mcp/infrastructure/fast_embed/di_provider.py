from dishka import Provider, provide, Scope

from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.infrastructure.fast_embed.config import FastembedEmbedderConfig
from vdb_mcp.infrastructure.fast_embed.embedder import FastembedEmbedder


class FastembedEmbedderProvider(Provider):
    """Dependecy provider for Fastembed embedder."""

    @provide(scope=Scope.APP)
    def fastembed_config(self) -> FastembedEmbedderConfig:
        """Get Fastembed embedder config."""
        return FastembedEmbedderConfig()  # type: ignore[missing-argument]

    @provide(scope=Scope.APP)
    def fastembed_embedder(
        self,
        fastembed_config: FastembedEmbedderConfig,
    ) -> Embedder:
        """Get Fastembed embedder."""
        return FastembedEmbedder(
            fastembed_config.model_name,
            fastembed_config.cache_dir,
            fastembed_config.threads,
        )

from typing import AsyncIterable

from dishka import Provider, Scope, provide
from openai import AsyncOpenAI

from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.infrastructure.open_ai.config import OpenAIEmbedderConfig
from vdb_mcp.infrastructure.open_ai.embedder import OpenAIEmbedder


class OpenAIEmbedderProvider(Provider):
    """Dependency provider for OpenAI embedder."""

    @provide(scope=Scope.APP)
    def openai_embedder_config(
        self,
    ) -> OpenAIEmbedderConfig:
        """Get OpenAI embedder config."""
        return OpenAIEmbedderConfig()  # type: ignore[missing-argument]

    @provide(scope=Scope.APP)
    async def openai_client(
        self,
        config: OpenAIEmbedderConfig,
    ) -> AsyncIterable[AsyncOpenAI]:
        """Get OpenAI client."""
        client = AsyncOpenAI(
            base_url=config.base_url,
            api_key=config.api_key,
            timeout=config.timeout,
            max_retries=config.max_retries,
        )

        try:
            yield client
        finally:
            await client.close()

    @provide(scope=Scope.APP)
    def openai_embedder(
        self,
        config: OpenAIEmbedderConfig,
        openai_client: AsyncOpenAI,
    ) -> Embedder:
        """Get OpenAI embedder."""
        return OpenAIEmbedder(
            openai_client,
            config.model,
        )

from openai import AsyncOpenAI

from vdb_mcp.application.ports.embedder import Embedder


class OpenAIEmbedder(Embedder):
    """OpenAI-compatible embedder."""

    def __init__(
        self,
        openai_client: AsyncOpenAI,
        model: str,
    ) -> None:
        """Initialize class object."""
        self._openai_client = openai_client
        self._model = model

    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""
        response = await self._openai_client.embeddings.create(
            input=text,
            model=self._model,
            encoding_format="float",
        )

        return response.data[0].embedding

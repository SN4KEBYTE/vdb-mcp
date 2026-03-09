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
        self._embedding_dimension: int | None = None

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

    async def get_embedding_dimension(
        self,
    ) -> int:
        """Get embedding vector dimension."""
        if self._embedding_dimension is not None:
            return self._embedding_dimension

        embedding = await self.embed("sample")
        self._embedding_dimension = len(embedding)

        return self._embedding_dimension

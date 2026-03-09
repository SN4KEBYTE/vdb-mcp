import asyncio

from fastembed import TextEmbedding

from vdb_mcp.application.ports.embedder import Embedder


class FastembedEmbedder(Embedder):
    """Embedder based on fastembed."""

    def __init__(
        self,
        model_name: str,
        cache_dir: str,
        threads: int,
    ) -> None:
        """Initialize class object."""
        self._model = TextEmbedding(
            model_name,
            cache_dir,
            threads,
            providers=["CPUExecutionProvider"],
        )
        self._embedding_dimension: int | None = None

    # TODO: different embeddings for query and passage
    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""
        embeddings = await asyncio.to_thread(
            lambda: list(self._model.embed([text]))
        )

        return embeddings[0].tolist()

    async def get_embedding_dimension(
        self,
    ) -> int:
        """Get embedding vector dimension."""
        if self._embedding_dimension is not None:
            return self._embedding_dimension

        embeddings = await asyncio.to_thread(
            lambda: list(self._model.embed(["sample"]))
        )
        self._embedding_dimension = len(embeddings[0].tolist())

        return self._embedding_dimension

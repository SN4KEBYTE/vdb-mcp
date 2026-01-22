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

    # TODO: different embeddings for query and passage
    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(
            None,
            lambda: list(self._model.embed([text]))
        )

        return embeddings[0].tolist()

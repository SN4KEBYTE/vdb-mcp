from typing import Protocol


class Embedder(Protocol):
    """Embedder protocol."""

    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""

    async def get_embedding_dimension(
        self,
    ) -> int:
        """Get embedding vector dimension."""

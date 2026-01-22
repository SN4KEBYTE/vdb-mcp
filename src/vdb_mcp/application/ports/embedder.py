from typing import Protocol


class Embedder(Protocol):
    """Embedder protocol."""

    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""

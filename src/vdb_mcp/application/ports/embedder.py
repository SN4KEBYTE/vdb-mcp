from typing import Protocol


# todo: add method for getting embedding dimension
class Embedder(Protocol):
    """Embedder protocol."""

    async def embed(
        self,
        text: str,
    ) -> list[int | float]:
        """Embed text."""

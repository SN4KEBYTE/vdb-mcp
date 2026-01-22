from typing import Protocol


class VectorStore(Protocol):
    """Vector store protocol."""

    # TODO: schema
    async def create_collection(
        self,
        collection_name: str,
    ) -> None:
        """Create collection."""

    async def delete_collection(
        self,
        collection_name: str,
    ) -> None:
        """Delete collection."""

    async def insert_one(
        self,
        collection_name: str,
        embedding: list[int | float],
    ) -> None:
        """Insert single embedding into collection."""

    async def search(
        self,
        collection_name: str,
        query_embedding: list[int | float],
    ) -> None:
        """Run vector search in collection."""

from typing import Protocol, Any

from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    """Model that represents single search result."""

    document: str = Field()
    metadata: dict[str, Any] | None = Field(default=None)


class VectorStore(Protocol):
    """Vector store protocol."""

    async def create_collection(
        self,
        collection_name: str,
        embedding_dim: int,
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
        text: str,
        embedding: list[int | float],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Insert single embedding into collection."""

    async def search(
        self,
        collection_name: str,
        query_embedding: list[int | float],
        limit: int,
    ) -> list[SearchResult]:
        """Run vector search in collection."""

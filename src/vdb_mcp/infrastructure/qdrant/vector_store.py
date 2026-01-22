from qdrant_client import AsyncQdrantClient

from vdb_mcp.application.ports.vector_store import VectorStore


class QdrantVectorStore(VectorStore):
    def __init__(
        self,
        client: AsyncQdrantClient,
    ) -> None:
        self._client = client

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

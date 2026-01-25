from typing import Any
from uuid import uuid4

from qdrant_client import AsyncQdrantClient
from qdrant_client.conversions.common_types import VectorParams, Distance, PointStruct

from vdb_mcp.application.ports.vector_store import VectorStore, SearchResult


class QdrantVectorStore(VectorStore):
    """Qdrant vector store."""

    def __init__(
        self,
        client: AsyncQdrantClient,
    ) -> None:
        """Initialize class object."""
        self._client = client

    async def create_collection(
        self,
        collection_name: str,
        embedding_dim: int,
    ) -> None:
        """Create collection."""
        # TODO: payload index?
        await self._client.create_collection(
            collection_name,
            vectors_config=VectorParams(
                size=embedding_dim,
                distance=Distance.COSINE,
            ),
        )

    async def delete_collection(
        self,
        collection_name: str,
    ) -> None:
        """Delete collection."""
        await self._client.delete_collection(collection_name)

    async def insert_one(
        self,
        collection_name: str,
        text: str,
        embedding: list[int | float],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Insert single embedding into collection."""
        await self._client.upsert(
            collection_name,
            [
                PointStruct(
                    id=uuid4().hex,
                    vector=embedding,
                    payload={
                        "document": text,
                        "metadata": metadata,
                    },
                ),
            ]
        )

    async def search(
        self,
        collection_name: str,
        query_embedding: list[int | float],
        limit: int = 10,
    ) -> list[SearchResult]:
        """Run vector search in collection."""
        search_results = await self._client.query_points(
            collection_name=collection_name,
            query=query_embedding,  # type: ignore[arg-type]
            limit=limit,
        )

        return [
            SearchResult(
                document=point.payload["document"],
                metadata=point.payload.get("metadata"),
            )
            for point in search_results.points
        ]

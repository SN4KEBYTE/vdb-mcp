from typing import Any
from uuid import uuid4

from weaviate import WeaviateAsyncClient
from weaviate.classes.config import Configure, DataType, Property

from vdb_mcp.application.ports.vector_store import SearchResult, VectorStore


class WeaviateVectorStore(VectorStore):
    """Weaviate vector store."""

    def __init__(
        self,
        client: WeaviateAsyncClient,
    ) -> None:
        """Initialize class object."""
        self._client = client

    async def create_collection(
        self,
        collection_name: str,
        embedding_dim: int,
    ) -> None:
        """Create collection."""
        exists = await self._client.collections.exists(collection_name)
        if exists:
            return

        await self._client.collections.create(
            name=collection_name,
            vectorizer_config=Configure.Vectorizer.none(),
            properties=[
                Property(name="document", data_type=DataType.TEXT),
                Property(name="metadata", data_type=DataType.OBJECT),
            ],
        )

    async def delete_collection(
        self,
        collection_name: str,
    ) -> None:
        """Delete collection."""
        await self._client.collections.delete(collection_name)

    async def insert_one(
        self,
        collection_name: str,
        text: str,
        embedding: list[int | float],
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Insert single embedding into collection."""
        collection = self._client.collections.get(collection_name)
        await collection.data.insert(
            uuid=uuid4().hex,
            properties={
                "document": text,
                "metadata": metadata,
            },
            vector=embedding,
        )

    async def search(
        self,
        collection_name: str,
        query_embedding: list[int | float],
        limit: int = 10,
    ) -> list[SearchResult]:
        """Run vector search in collection."""
        collection = self._client.collections.get(collection_name)
        search_results = await collection.query.near_vector(
            near_vector=query_embedding,
            limit=limit,
            return_properties=["document", "metadata"],
        )

        return [
            SearchResult(
                document=(result.properties or {}).get("document", ""),
                metadata=(result.properties or {}).get("metadata"),
            )
            for result in search_results.objects
            if result.properties is not None
        ]

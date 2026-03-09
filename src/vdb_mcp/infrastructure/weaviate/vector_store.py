from typing import Any, cast
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
                Property(
                    name="document",
                    data_type=DataType.TEXT,  # type: ignore[unknown-argument]
                ),
                Property(
                    name="metadata",
                    data_type=DataType.OBJECT,  # type: ignore[unknown-argument]
                ),
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

        results: list[SearchResult] = []
        for result in search_results.objects:
            properties = result.properties
            if not isinstance(properties, dict):
                continue

            document = properties.get("document")
            if not isinstance(document, str):
                continue

            metadata = properties.get("metadata")
            if metadata is not None and not isinstance(metadata, dict):
                metadata = None

            results.append(
                SearchResult(
                    document=document,
                    metadata=cast(dict[str, Any] | None, metadata),
                )
            )

        return results

from typing import Any

from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.application.ports.vector_store import VectorStore


class SearchUsecase:
    """Search in collection use case."""

    def __init__(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> None:
        """Initialize the use case."""
        self._vector_storage = vector_storage
        self._embedder = embedder

    async def search(
        self,
        collection_name: str,
        text: str,
        limit: int = 10,
    ) -> str:
        """Search documents in a vector collection."""
        if limit <= 0:
            raise ValueError("limit must be greater than 0")

        embedding = await self._embedder.embed(text)
        search_results = await self._vector_storage.search(
            collection_name,
            embedding,
            limit,
        )

        if not search_results:
            return (
                f"No results found in collection '{collection_name}' for query: {text}"
            )

        def _format_result(
            index: int,
            document: str,
            metadata: dict[str, Any] | None,
        ) -> str:
            if metadata is None:
                return f"{index}. {document}"

            return f"{index}. {document}\n   metadata: {metadata}"

        formatted_results = "\n".join(
            _format_result(index, result.document, result.metadata)
            for index, result in enumerate(search_results, start=1)
        )
        return (
            f"Found {len(search_results)} results in collection '{collection_name}' "
            f"for query: {text}\n{formatted_results}"
        )

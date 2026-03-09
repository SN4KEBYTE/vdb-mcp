from vdb_mcp.application.ports.vector_store import VectorStore


class DeleteCollectionUsecase:
    """Delete collection use case."""

    def __init__(
        self,
        vector_storage: VectorStore,
    ) -> None:
        """Initialize the use case."""
        self._vector_storage = vector_storage

    async def delete_collection(
        self,
        collection_name: str,
    ) -> str:
        """Delete a vector collection."""
        await self._vector_storage.delete_collection(collection_name)

        return f"Collection '{collection_name}' deleted successfully."

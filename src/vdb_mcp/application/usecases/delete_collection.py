from vdb_mcp.application.ports.vector_store import VectorStore


class DeleteCollectionUsecase:
    def __init__(
        self,
        vector_storage: VectorStore,
    ) -> None:
        self._vector_storage = vector_storage

    # TODO: return msg for llm
    async def delete_collection(
        self,
        collection_name: str,
    ) -> str:
        await self._vector_storage.delete_collection(collection_name)

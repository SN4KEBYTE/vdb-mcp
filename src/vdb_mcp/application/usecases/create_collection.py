from vdb_mcp.application.ports.vector_store import VectorStore


class CreateCollectionUsecase:
    def __init__(
        self,
        vector_storage: VectorStore,
    ) -> None:
        self._vector_storage = vector_storage

    # TODO: return msg for llm
    async def create_collection(
        self,
        collection_name: str,
    ) -> str:
        await self._vector_storage.create_collection(collection_name)

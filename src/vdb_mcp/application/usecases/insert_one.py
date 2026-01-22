from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.application.ports.vector_store import VectorStore


class InsertOneUsecase:
    def __init__(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> None:
        self._vector_storage = vector_storage
        self._embedder = embedder

    # TODO: return msg for llm
    async def insert_one(
        self,
        text: str,
        collection_name: str,
    ) -> str:
        """Insert single embedding into collection."""
        embedding = await self._embedder.embed(text)
        await self._vector_storage.insert_one(
            collection_name,
            embedding,
        )

        return ""

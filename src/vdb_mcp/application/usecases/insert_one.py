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

    async def insert_one(
        self,
        text: str,
        collection_name: str,
    ) -> str:
        """Insert single embedding into collection."""
        embedding = await self._embedder.embed(text)
        await self._vector_storage.insert_one(
            collection_name,
            text,
            embedding,
        )

        return f"Document inserted into collection '{collection_name}' successfully."

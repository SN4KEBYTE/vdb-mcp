from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.application.ports.vector_store import VectorStore


class CreateCollectionUsecase:
    def __init__(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> None:
        self._vector_storage = vector_storage
        self._embedder = embedder

    async def create_collection(
        self,
        collection_name: str,
    ) -> str:
        embedding_dimension = await self._embedder.get_embedding_dimension()
        await self._vector_storage.create_collection(
            collection_name,
            embedding_dimension,
        )

        return (
            f"Collection '{collection_name}' created successfully "
            f"with embedding dimension {embedding_dimension}."
        )

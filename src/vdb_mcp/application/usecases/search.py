from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.application.ports.vector_store import VectorStore


class SearchUsecase:
    def __init__(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> None:
        self._vector_storage = vector_storage
        self._embedder = embedder

    # TODO: search params, format result
    # TODO: maybe use fixed collection_name?
    async def search(
        self,
        collection_name: str,
        text: str,
    ) -> list[str] | None:
        embedding = await self._embedder.embed(text)
        search_result = await self._vector_storage.search(
            collection_name,
            embedding,
        )

        return ""

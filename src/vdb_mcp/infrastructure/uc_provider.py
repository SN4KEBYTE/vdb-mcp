from dishka import Provider, provide, Scope

from vdb_mcp.application.ports.embedder import Embedder
from vdb_mcp.application.ports.vector_store import VectorStore
from vdb_mcp.application.usecases.create_collection import CreateCollectionUsecase
from vdb_mcp.application.usecases.delete_collection import DeleteCollectionUsecase
from vdb_mcp.application.usecases.insert_one import InsertOneUsecase
from vdb_mcp.application.usecases.search import SearchUsecase


class UsecasesProvider(Provider):
    @provide(scope=Scope.APP)
    def create_collection_usecase(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> CreateCollectionUsecase:
        return CreateCollectionUsecase(
            vector_storage,
            embedder,
        )

    @provide(scope=Scope.APP)
    def delete_collection_usecase(
        self,
        vector_storage: VectorStore,
    ) -> DeleteCollectionUsecase:
        return DeleteCollectionUsecase(vector_storage)

    @provide(scope=Scope.APP)
    def insert_one_usecase(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> InsertOneUsecase:
        return InsertOneUsecase(
            vector_storage,
            embedder,
        )

    @provide(scope=Scope.APP)
    def search_usecase(
        self,
        vector_storage: VectorStore,
        embedder: Embedder,
    ) -> SearchUsecase:
        return SearchUsecase(
            vector_storage,
            embedder,
        )

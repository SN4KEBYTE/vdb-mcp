from typing import Annotated

from dishka import FromDishka
from fastmcp import Context
from pydantic import Field

from vdb_mcp.application.usecases.create_collection import CreateCollectionUsecase
from vdb_mcp.application.usecases.delete_collection import DeleteCollectionUsecase
from vdb_mcp.application.usecases.insert_one import InsertOneUsecase
from vdb_mcp.application.usecases.search import SearchUsecase
from vdb_mcp.presentation.mcp.dishka_integration import inject


@inject
async def create_collection(
    ctx: Context,
    collection_name: Annotated[
        str,
        Field(description="The collection to create"),
    ],
    create_collection_uc: FromDishka[CreateCollectionUsecase],
) -> str:
    """Tool for creating collection."""
    return await create_collection_uc.create_collection(collection_name)


@inject
async def delete_collection(
    ctx: Context,
    collection_name: Annotated[
        str,
        Field(description="The collection to delete"),
    ],
    delete_collection_uc: FromDishka[DeleteCollectionUsecase],
) -> str:
    """Tool for deleting collection."""
    return await delete_collection_uc.delete_collection(collection_name)


@inject
async def search(
    ctx: Context,
    query: Annotated[
        str,
        Field(description="What to search for"),
    ],
    collection_name: Annotated[
        str,
        Field(description="The collection to search in"),
    ],
    search_uc: FromDishka[SearchUsecase],
) -> list[str] | None:
    """Tool for searching in collection."""
    return await search_uc.search(
        collection_name,
        query,
    )


@inject
async def insert_one(
    ctx: Context,
    information: Annotated[
        str,
        Field(description="Text to store"),
    ],
    collection_name: Annotated[
        str,
        Field(description="The collection to store the information in"),
    ],
    insert_one_uc: FromDishka[InsertOneUsecase],
) -> str:
    """Tool for insertion into collection."""
    return await insert_one_uc.insert_one(
        information,
        collection_name,
    )

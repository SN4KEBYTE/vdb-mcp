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
    create_collection_uc: FromDishka[CreateCollectionUsecase],
    collection_name: Annotated[
        str,
        Field(description="The collection to create"),
    ],
) -> str:
    """Tool for creating collection."""
    return await create_collection_uc.create_collection(collection_name)


@inject
async def delete_collection(
    ctx: Context,
    delete_collection_uc: FromDishka[DeleteCollectionUsecase],
    collection_name: Annotated[
        str,
        Field(description="The collection to delete"),
    ],
) -> str:
    """Tool for deleting collection."""
    return await delete_collection_uc.delete_collection(collection_name)


@inject
async def search(
    ctx: Context,
    search_uc: FromDishka[SearchUsecase],
    query: Annotated[
        str,
        Field(description="What to search for"),
    ],
    collection_name: Annotated[
        str,
        Field(description="The collection to search in"),
    ],
    limit: Annotated[
        int,
        Field(description="Maximum number of search results to return", ge=1),
    ] = 10,
) -> str:
    """Tool for searching in collection."""
    return await search_uc.search(
        collection_name,
        query,
        limit,
    )


@inject
async def insert_one(
    ctx: Context,
    insert_one_uc: FromDishka[InsertOneUsecase],
    information: Annotated[
        str,
        Field(description="Text to store"),
    ],
    collection_name: Annotated[
        str,
        Field(description="The collection to store the information in"),
    ],
) -> str:
    """Tool for insertion into collection."""
    return await insert_one_uc.insert_one(
        information,
        collection_name,
    )

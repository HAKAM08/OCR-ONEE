from fastapi import APIRouter

from app.elasticsearch.search_service import SearchService


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search_documents(q: str):

    return SearchService.search(q)
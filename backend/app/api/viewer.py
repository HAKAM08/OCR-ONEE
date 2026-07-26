from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.viewer import ViewerResponse

from app.services.viewer_service import ViewerService


router = APIRouter(

    prefix="/viewer",

    tags=["Viewer"]

)


@router.get(

    "/{document_id}",

    response_model=ViewerResponse

)
def get_document(

    document_id: int,

    db: Session = Depends(get_db)

):

    try:

        return ViewerService.get_document(
            db,
            document_id
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
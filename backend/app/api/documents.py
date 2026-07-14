from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.document import DocumentResponse
from app.services.background_task_service import BackgroundTaskService
from app.services.document_service import DocumentService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/upload",
    response_model=DocumentResponse
)
def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    document = DocumentService.upload_document(
        db=db,
        file=file,
        owner_id=1
    )

    BackgroundTaskService.start_document_processing(
        background_tasks,
        document.id
    )

    return document
from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import Query
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.document import DocumentResponse

from app.services.background_task_service import BackgroundTaskService
from app.services.document_service import DocumentService


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    document = DocumentService.upload_document(
        db=db,
        file=file,
        owner_id=1,
    )

    BackgroundTaskService.start_document_processing(
        background_tasks,
        document.id,
    )

    return document


@router.get("")
def get_documents(
    db: Session = Depends(get_db),
):

    return DocumentService.get_all_documents(db)


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    return DocumentService.get_document(
        db,
        document_id,
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    try:

        DocumentService.delete_document(
            db,
            document_id,
        )

        return {
            "message": "Document deleted successfully."
        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
        
@router.get("/{document_id}/status")
def get_document_status(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = DocumentService.get_document(
        db,
        document_id,
    )

    return {
        "id": document.id,
        "status": document.status,
    }
    
@router.get("/{document_id}/thumbnail")
def get_thumbnail(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = DocumentService.get_document(
        db,
        document_id,
    )

    return {
        "id": document.id,
        "file_type": document.file_type,
        "thumbnail": f"/uploads/documents/{document.filename}",
    }
@router.get("")
def get_documents(

    page: int = Query(1, ge=1),

    page_size: int = Query(10, ge=1, le=100),

    db: Session = Depends(get_db),

):

    return DocumentService.get_paginated_documents(

        db,

        page,

        page_size,

    )
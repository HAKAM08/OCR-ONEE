from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    File,
    Form,
    HTTPException,
    Query,
    UploadFile,
)
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.session import get_db
from app.enums.document_type import DocumentType
from app.models.user import User
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
    document_type: DocumentType = Form(DocumentType.COMMON),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if (
        current_user.role != "ADMIN"
        and document_type == DocumentType.CONFIDENTIAL
    ):
        raise HTTPException(
            status_code=403,
            detail="Only administrators can upload confidential documents.",
        )

    document = DocumentService.upload_document(
        db=db,
        file=file,
        owner_id=current_user.id,
        document_type=document_type,
    )

    BackgroundTaskService.start_document_processing(
        background_tasks,
        document.id,
    )

    return document


@router.get("")
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return DocumentService.get_all_documents(
        db=db,
        current_user=current_user,
    )
    
@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
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
    current_user: User = Depends(get_current_user),
):

    document = DocumentService.get_document(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )
    return {
        "id": document.id,
        "status": document.status,
    }


@router.get("/{document_id}/thumbnail")
def get_thumbnail(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    document = DocumentService.get_document(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )

    return {
        "id": document.id,
        "file_type": document.file_type,
        "thumbnail": f"/uploads/documents/{document.filename}",
    }
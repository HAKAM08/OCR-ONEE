from fastapi import FastAPI

from app.api.dashboard import router as dashboard_router
from app.api.auth import router as auth_router
from app.api.documents import router as document_router
from app.api.ocr import router as ocr_router
from app.elasticsearch.mapping import MappingService
from contextlib import asynccontextmanager
from app.api.search import router as search_router
from app.api.viewer import router as viewer_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

@asynccontextmanager
async def lifespan(app: FastAPI):

    MappingService.create_index()

    yield

app = FastAPI(
    title="ONEE OCR Document Management API",
    version="1.0.0",
    lifespan=lifespan
)

app.mount(
    "/uploads",
    StaticFiles(directory="app/uploads"),
    name="uploads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(document_router)
app.include_router(ocr_router)
app.include_router(dashboard_router)
app.include_router(viewer_router)


@app.get("/")
def root():
    return {
        "message": "Bienvenue dans l'API OCR de l'ONEE"
    }
    
app.include_router(search_router)
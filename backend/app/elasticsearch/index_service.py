from app.core.config import settings
from app.elasticsearch.client import ElasticsearchClient


class IndexService:
    """
    Responsible for indexing OCR results.
    """

    @staticmethod
    def index_document(document, ocr_result):

        client = ElasticsearchClient.get_client()

        client.index(

            index=settings.ELASTICSEARCH_INDEX,

            id=document.id,

            document={

                "document_id": document.id,

                "filename": document.original_filename,

                "text": ocr_result.text,

                "language": ocr_result.language,

                "confidence": ocr_result.confidence,

                "page_count": ocr_result.page_count,

                "upload_date": document.upload_date

            }

        )
from app.core.config import settings
from app.elasticsearch.client import ElasticsearchClient


class MappingService:
    """
    Creates the Elasticsearch index
    if it does not already exist.
    """

    @staticmethod
    def create_index():

        client = ElasticsearchClient.get_client()

        if client.indices.exists(
            index=settings.ELASTICSEARCH_INDEX
        ):
            return

        mapping = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "default": {
                            "type": "standard"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {

                    "document_id": {
                        "type": "integer"
                    },

                    "filename": {
                        "type": "text"
                    },

                    "text": {
                        "type": "text"
                    },

                    "language": {
                        "type": "keyword"
                    },

                    "confidence": {
                        "type": "float"
                    },

                    "page_count": {
                        "type": "integer"
                    },

                    "upload_date": {
                        "type": "date"
                    }

                }
            }
        }

        client.indices.create(
            index=settings.ELASTICSEARCH_INDEX,
            body=mapping
        )
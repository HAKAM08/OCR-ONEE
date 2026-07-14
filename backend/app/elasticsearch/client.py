from elasticsearch import Elasticsearch

from app.core.config import settings


class ElasticsearchClient:
    """
    Singleton Elasticsearch client.
    """

    _client = None

    @classmethod
    def get_client(cls) -> Elasticsearch:

        if cls._client is None:

            cls._client = Elasticsearch(
                settings.ELASTICSEARCH_URL,
                request_timeout=30
            )

        return cls._client
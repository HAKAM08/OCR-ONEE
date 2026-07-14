from app.core.config import settings
from app.elasticsearch.client import ElasticsearchClient


class SearchService:
    """
    Service responsible for searching documents
    stored in Elasticsearch.
    """

    @staticmethod
    def search(query: str):

        client = ElasticsearchClient.get_client()

        response = client.search(

            index=settings.ELASTICSEARCH_INDEX,

            query={
                "multi_match": {
                    "query": query,
                    "fields": [
                        "text^3",
                        "filename^2",
                        "language"
                    ]
                }
            },

            highlight={
                "fields": {
                    "text": {}
                }
            }

        )

        return response["hits"]["hits"]
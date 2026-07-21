from app.core.config import settings
from app.elasticsearch.client import ElasticsearchClient


class SearchService:
    """
    Responsible for searching indexed OCR documents.
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

                    ],

                    "fuzziness": "AUTO"

                }

            },

            highlight={

                "fields": {

                    "text": {},

                    "filename": {}

                }

            }

        )

        results = []

        for hit in response["hits"]["hits"]:

            source = hit["_source"]

            highlight = hit.get("highlight", {})

            snippet = ""

            if "text" in highlight:

                snippet = "... ".join(highlight["text"])

            else:

                snippet = source["text"][:250]

            results.append({

                "id": source["document_id"],

                "filename": source["filename"],

                "language": source["language"],

                "confidence": source["confidence"],

                "page_count": source["page_count"],

                "upload_date": source["upload_date"],

                "score": hit["_score"],

                "snippet": snippet

            })

        return results
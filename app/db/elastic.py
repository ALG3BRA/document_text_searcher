from elasticsearch import AsyncElasticsearch
from config import ELASTIC_PASSWORD


client = AsyncElasticsearch(
    "https://es:9200",
    verify_certs=False,
    basic_auth=("elastic", ELASTIC_PASSWORD),
)

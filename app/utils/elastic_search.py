from elasticsearch import AsyncElasticsearch

ELASTIC_PASSWORD = "RcPWldykfXEaDjfqzAse"

client = AsyncElasticsearch(
    "https://elasticsearch:9200",
    verify_certs=False,
    basic_auth=("elastic", ELASTIC_PASSWORD),
)


async def add_document_to_index(doc_id: int, text: str):
    document = {"text": text}
    await client.index(index="documents_index", id=doc_id, body=document)


async def search_documents(query: str):
    search_body = {
        "query": {
            "match": {"text": query}
        }
    }
    result = await client.search(index="documents_index", body=search_body)
    print(result)
    return result['hits']['hits']


async def delete_document_from_index(doc_id: int):
    await client.delete(index="documents_index", id=doc_id)

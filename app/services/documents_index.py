from repositories.elastic_repo import AbstractIndexRepository


class DocumentsIndexService:
    def __init__(self, index_repo: AbstractIndexRepository):
        self.repo = index_repo()

    async def search(self, *matches):
        docs = await self.repo.search(*matches)
        return docs

    async def add_one(self, _id, *query):
        await self.repo.add_one(_id, *query)

    async def delete_one(self, _id):
        await self.repo.delete_one(_id)


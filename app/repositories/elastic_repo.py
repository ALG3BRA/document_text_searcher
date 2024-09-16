from abc import ABC, abstractmethod
from models.base_index_model import BaseIndexModel
from db.elastic import client


class AbstractIndexRepository(ABC):
    @abstractmethod
    async def search(self, *matches):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, id, *query):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id):
        raise NotImplementedError


class ElasticRepository(AbstractIndexRepository):
    model: BaseIndexModel = None

    async def search(self, *matches):
        search_body = {
            "match": {key: item for key, item in zip(self.model.body_content, matches)}
        }
        result = await client.search(index=self.model.index, query=search_body)
        return result['hits']['total']

    async def add_one(self, _id, *query):
        body = dict()
        for key, item in zip(self.model.body_content, query):
            body[key] = item

        await client.index(index=self.model.index, id=_id, document=body)

    async def delete_one(self, _id):
        client.delete(index=self.model.index, id=_id)

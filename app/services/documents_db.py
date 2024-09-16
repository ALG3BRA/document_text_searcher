from utils.uow import AbstractUOW


class DocumentsSQLService:
    @staticmethod
    async def get(uow: AbstractUOW, ids, limit: int = 20, order_by: str = "created_date"):
        docs = await uow.documents.get_by_ids(ids, order_by, limit)
        return docs

    @staticmethod
    async def add_one(uow: AbstractUOW, text, rubrics):
        doc_id = await uow.documents.add_one(text=text, rubrics=rubrics)
        return doc_id

    @staticmethod
    async def delete_one(uow: AbstractUOW, doc_id):
        await uow.documents.delete_one(doc_id)


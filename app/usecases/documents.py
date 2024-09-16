from abc import ABC, abstractmethod

from repositories.documents import DocumentsIndexRepo
from utils.dependencies import UOWDep
from services.documents_index import DocumentsIndexService
from services.documents_db import DocumentsSQLService


class AbstractDocumentsUseCase(ABC):
    @abstractmethod
    async def find_documents(self, text): ...

    @abstractmethod
    async def add_document(self, text, rubrics): ...

    @abstractmethod
    async def delete_document(self, doc_id): ...


class DocumentsUseCase:
    index_service = DocumentsIndexService(DocumentsIndexRepo)

    def __init__(self, uow: UOWDep):
        self.uow = uow

    async def find_documents(self, text):
        async with self.uow as uow:
            es_results = await self.index_service.search(text)

            doc_ids = [hit["_id"] for hit in es_results]

            if doc_ids:
                db_result = await DocumentsSQLService.get(uow, doc_ids)
                await uow.commit()
                return db_result
            return

    async def add_document(self, text, rubrics):
        async with self.uow as uow:
            try:
                doc_id = await DocumentsSQLService.add_one(uow, text, rubrics)
                await self.index_service.add_one(doc_id, text)
                await uow.commit()
            except Exception as err:
                await uow.rollback()
                raise err

    async def delete_document(self, doc_id):
        async with self.uow as uow:
            try:
                await DocumentsSQLService.delete_one(uow, doc_id)
                await self.index_service.delete_one(doc_id)
                await uow.commit()
            except Exception as err:
                await uow.rollback()
                raise err

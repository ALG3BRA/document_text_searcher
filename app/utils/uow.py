from abc import ABC, abstractmethod

from db.postgres import async_session_maker
from repositories.documents import DocumentsSQLRepo


class AbstractUOW(ABC):
    documents = None

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UOW:
    async def __aenter__(self):
        self.session = async_session_maker()
        self.documents = DocumentsSQLRepo(self.session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

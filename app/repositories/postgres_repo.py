from abc import ABC, abstractmethod
from sqlalchemy import insert, select, desc, delete
from db.postgres import async_session_maker


class AbstractDatabaseRepository(ABC):
    @abstractmethod
    async def get_by_ids(self, ids, limit, order_by):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, data):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self, doc_id):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractDatabaseRepository):
    model = None

    def __init__(self, session):
        self.session = session

    async def get_by_ids(self, ids, order_by, limit=100):
        stmt = select(self.model).where(self.model.id.in_(ids))

        if order_by:
            stmt = stmt.order_by(order_by)

        stmt = stmt.limit(limit)

        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def add_one(self, **data):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def delete_one(self, id):
        stmt = delete(self.model).where(self.model.id == id)
        await self.session.execute(stmt)

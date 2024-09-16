from models.documents import SQLDocument, IndexDocument
from repositories.postgres_repo import SQLAlchemyRepository
from repositories.elastic_repo import ElasticRepository


class DocumentsSQLRepo(SQLAlchemyRepository):
    model = SQLDocument


class DocumentsIndexRepo(ElasticRepository):
    model = IndexDocument

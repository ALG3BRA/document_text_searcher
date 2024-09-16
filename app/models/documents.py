import uuid
from datetime import datetime
from sqlalchemy import UUID, Column, ARRAY, String, TIMESTAMP
from models.base_index_model import BaseIndexModel
from models.base import Base


class SQLDocument(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rubrics = Column(ARRAY(String))
    text = Column(String)
    created_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)


class IndexDocument(BaseIndexModel):
    index = "documents_index"
    body_content = ["text"]

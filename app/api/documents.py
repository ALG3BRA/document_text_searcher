import uuid
from typing import List

from fastapi import APIRouter
from db.postgres import init_db
from usecases.dependencies import DocumentCase


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


'''@router.on_event("startup")
async def startup():
    await init_db()'''


@router.get("", response_model=None)
async def get_documents(text, document_case: DocumentCase):
    docs = await document_case.find_documents(text)
    return docs


@router.post("", response_model=None)
async def create_document(text: str, rubrics: List[str],
                          document_case: DocumentCase):
    await document_case.add_document(text, rubrics)


@router.delete("")
async def delete_document(doc_id: uuid.UUID, document_case: DocumentCase):
    await document_case.delete_document(doc_id)
    return "Successfully deleted"
















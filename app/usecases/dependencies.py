from typing import Annotated

from fastapi import Depends

from usecases.documents import AbstractDocumentsUseCase, DocumentsUseCase

DocumentCase = Annotated[AbstractDocumentsUseCase, Depends(DocumentsUseCase)]

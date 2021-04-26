from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import ImagesDB, ImagesSchema

router = APIRouter()


@router.post("/", response_model=ImagesDB, status_code=201)
async def create_image(payload: ImagesSchema):
    note_id = await crud.post_image(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
        "link_to_file": payload.link_to_file,
    }
    return response_object

from app.api.models import NoteSchema, ImagesSchema
from app.db import notes, images, database


async def post_note(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def post_image(payload: ImagesSchema):
    query = images.insert().values(title=payload.title, description=payload.description,
                                   link_to_file=payload.link_to_file)
    return await database.execute(query=query)

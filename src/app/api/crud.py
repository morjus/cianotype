from app.api.models import NoteSchema, ImagesSchema
from app.db import notes, images, database


async def post_note(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def post_image(payload: ImagesSchema):
    query = images.insert().values(title=payload.title, description=payload.description,
                                   link_to_file=payload.link_to_file)
    return await database.execute(query=query)


async def get_note(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all_notes():
    query = notes.select()
    return await database.fetch_all(query=query)


async def put_note(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


async def delete_note(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)

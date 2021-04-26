from pydantic import BaseModel


class ImagesSchema(BaseModel):
    title: str
    description: str
    link_to_file: str


class ImagesDB(ImagesSchema):
    id: int


class NoteSchema(BaseModel):
    title: str
    description: str


class NoteDB(NoteSchema):
    id: int

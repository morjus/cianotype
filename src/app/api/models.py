from pydantic import BaseModel, Field


class ImagesSchema(BaseModel):
    title: str
    description: str
    link_to_file: str


class ImagesDB(ImagesSchema):
    id: int


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class NoteDB(NoteSchema):
    id: int

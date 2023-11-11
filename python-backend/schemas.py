from pydantic import BaseModel, ConfigDict, Field

class ExcursionDto(BaseModel):
    id_: int = Field(..., description="Identifier", alias="id")
    name: str
    short_description: str
    description: str
    duration: int
    person: str
    person_photo_path: str

    model_config = ConfigDict(from_attributes=True, json_schema_extra={"examples":[{"name":"Anne Frank","id":0,"short_description":"Something interesting","description":"Something really interesting","duration":90,"person":"Ivan Smirnov","person_photo_path":"static/photos"}]})
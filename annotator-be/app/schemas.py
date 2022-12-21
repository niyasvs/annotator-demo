from datetime import datetime
from typing import List, Any
from pydantic import BaseModel, EmailStr, constr,Field
from bson.objectid import ObjectId


class UserBaseSchema(BaseModel):
    name: str
    email: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema


class FilteredUserResponse(UserBaseSchema):
    id: str

class ProjectBaseSchema(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CreateProjectSchema(ProjectBaseSchema):
    user: ObjectId | None = None
    pass

class ImageBaseSchema(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    annotations: List[Any]
    name: str
    project: ObjectId | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}



class ImageResponse(ImageBaseSchema):
    id: str
    created_at: datetime
    updated_at: datetime


class UpdateAnnotation(BaseModel):
    annotations: List[Any]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListImagesResponse(BaseModel):
    status: str
    results: int
    images: List[ImageResponse]

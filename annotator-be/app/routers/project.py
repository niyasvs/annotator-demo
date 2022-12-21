from app import schemas
from app.oauth2 import require_user
from app.serializers.projectSerializers import projectListEntity
from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from app.database import Project
import os
from bson.objectid import ObjectId

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_project(payload: schemas.CreateProjectSchema, request: Request, user_id: str = Depends(require_user)):
    payload.user = ObjectId(user_id)
    created = Project.insert_one(payload.dict())
    os.mkdir(f'projects/{str(created.inserted_id)}')
    return {'status': 'success', 'message': 'successfully created'}

@router.get('/')
def get_projects(user_id: str = Depends(require_user)):
    pipeline = [
        {'$match': {"user": {"$eq":ObjectId(user_id)}}},
    ]
    projects = projectListEntity(Project.aggregate(pipeline))
    return {'status': 'success', 'results': len(projects), 'projects': projects}

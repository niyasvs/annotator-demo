from datetime import datetime
from typing import List
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from app import schemas
from app.database import Image
from app.oauth2 import require_user
from app.serializers.imageSerializers import imageEntity, imageListEntity
from bson.objectid import ObjectId
from fastapi import File, UploadFile

router = APIRouter()


@router.get('/{project_id}')
def get_images(project_id: str, user_id: str = Depends(require_user)):
    pipeline = [
        {'$match': {"project": {"$eq":ObjectId(project_id)}}},
    ]
    images = imageListEntity(Image.aggregate(pipeline))
    return {'status': 'success', 'results': len(images), 'images': images}


@router.post('/{project_id}', status_code=status.HTTP_201_CREATED)
def upload_images(project_id: str, files: List[UploadFile] = File(...), user_id: str = Depends(require_user)):
    for file in files:
        try:
            contents = file.file.read()
            name = file.filename
            image = schemas.ImageBaseSchema(
                name = name, 
                project= ObjectId(project_id),
                annotations = []
            )
            image.name = name
            image.project = ObjectId(project_id)
            image.annotations = []
            image.created_at = datetime.utcnow()
            image.updated_at = image.created_at
            result = Image.insert_one(image.dict())
            with open(f'projects/{project_id}/{result.inserted_id}.{name.split(".")[-1]}', 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()
    return {'status': 'success'}


@router.put('/{id}')
def update_annotations(id: str, payload: schemas.UpdateAnnotation, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid id: {id}")
    updated_image = Image.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_image:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No image with this id: {id} found')
    return imageEntity(updated_image)


@router.get('/find_one/{id}')
def get_image(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid id: {id}")
    pipeline = [
        {'$match': {'_id': ObjectId(id)}}
    ]
    image = imageListEntity(Image.aggregate(pipeline))[0]
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No image with this id: {id} found")
    return image


@router.delete('/{id}')
def delete_image(id: str, user_id: str = Depends(require_user)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid id: {id}")
    image = Image.find_one_and_delete({'_id': ObjectId(id)})
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No image with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)

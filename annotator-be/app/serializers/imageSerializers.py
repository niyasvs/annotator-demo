def imageEntity(image) -> dict:
    return {
        "id": str(image["_id"]),
        "name": image["name"],
        "project": str(image["project"]),
        "annotations": image["annotations"],
        "created_at": image["created_at"],
        "updated_at": image["updated_at"]
    }


def imageListEntity(images) -> list:
    return [imageEntity(image) for image in images]


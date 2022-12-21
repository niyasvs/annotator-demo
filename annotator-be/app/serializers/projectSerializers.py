def projectEntity(project) -> dict:
    return {
        "id": str(project["_id"]),
        "name": project["name"],
    }


def projectListEntity(projects) -> list:
    return [projectEntity(project) for project in projects]
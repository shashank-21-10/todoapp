def todoSerializer(Todo) -> dict:
    return {
        "_id":str(Todo["_id"]),
        "title":Todo["title"],
        "description":Todo["description"]
    }

def todoListSerializer(Todos):
    return [todoSerializer(Todo) for Todo in Todos]
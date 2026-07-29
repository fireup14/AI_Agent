from typing import TypedDict


class UserData(TypedDict):

    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age



def show_user(user: UserData) -> str:
    return f"{user['name']}: {user['age']}"



user = UserData(name="Alice", age=30)
print(show_user(user))
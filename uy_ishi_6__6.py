from fastapi import FastAPI , Path , Body
import uvicorn
from typing import Annotated
app = FastAPI()

@app.get("/")
def hello() -> dict:
    return {"message" : "Hello world"}

user=[
    {"id":1,"user": "Abdullayev Husanboy","age": 2008,"manzil": "Fergana"},
    {"id":2,"user": "Ali Aliyev","age": 2009,"manzil": "Andijon"},
    {"id":3,"user": "Vali valiyev","age": 2000,"manzil": "Samarqand"},
    {"id":4,"user": "Botir Botirov","age": 2010,"manzil": "Buxoro"},
    {"id":5,"user": "Qotir Qotirov","age": 2008,"manzil": "Fergana"}
]

@app.get("/users/")
def user_read() -> list[dict]:
    return user

@app.get("/users/{user_id}/")
def read_user(user_id: Annotated[int , Path(ge=1,le=5)]) -> dict:
    for users in user:
        if users.get("id") == user_id:
            return users

@app.get("/users/manzil/{user_manzil}/")
def read_user_by_manzil(user_manzil: str) -> list[dict]:
    result = []
    for users in user:
        if users["manzil"].lower() == user_manzil.lower():
            result.append(users)
    return result

        
@app.post("/users/")
def create_user(username: str = Body(), age: int = Body(), manzil: str = Body()) -> dict:
    user.append(
        {
            "id": len(user) + 1,
            "user": username,
            "age": age,
            "manzil": manzil
        }
    )
    return {"message": "User created successful!"}

@app.delete("/users/{user_id}/")
def delete_book(user_id: int) -> dict:
    for users in user:
        if users.get("id") == user_id:
            user.remove(users)
            return {"message" : "User delete successful!"}



if __name__ == '__main__':
    uvicorn.run(app,port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4

app = FastAPI()

class Todo(BaseModel):
    id: UUID
    title: str
    completed: bool

class TodoCreate(BaseModel):
    title: str
    completed: bool

todos = []

@app.get("/")
def home():
    adsda
    return {"status": "ok"}

@app.get("/todos")
def get_todos():
    asda
    return todos

@app.post("/todos")
def add_todo(todo: TodoCreate):
    jhj
    new_todo = Todo(
        id=uuid4(),
        title=todo.title,
        completed=todo.completed
    )
    todos.append(new_todo)
    return new_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    uygvuy
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos.pop(i)
            return {"status":"deleted"}
    
    return {"error": "Not found"}



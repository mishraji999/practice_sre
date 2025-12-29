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
    return {"status": "ok"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: TodoCreate):
    new_todo = Todo(
        id=uuid4(),
        title=todo.title,
        completed=todo.completed
    )
    todos.append(new_todo)
    return new_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: UUID):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos.pop(i)
            return {"status": "deleted"}
    return {"error": "Not found"}



@app.put("/todos/{todo_id}")
def update_todo(todo_id: UUID, updated: TodoCreate):
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos[i].title = updated.title
            todos[i].completed = updated.completed
            return todos[i]
    return {"error": "Not found"}


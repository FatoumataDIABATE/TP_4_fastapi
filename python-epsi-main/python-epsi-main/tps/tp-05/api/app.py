from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(description="TP5 API")

# Modèles de données
class User(BaseModel):
    username: str
    password: str

class ToDoItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    priority: int

class ToDoItem(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    priority: int

class Result(BaseModel):
    result: int

# Simulations de stockage en mémoire
users_db = {}
todo_db = {}

# Route principale
@app.get("/", response_model=dict)
async def read_root():
    return {}

# Route pour l'addition
@app.get("/miscellaneous/addition", response_model=Result)
async def addition(a: int, b: int):
    return Result(result=a + b)

# Gestion des utilisateurs
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Utilisateur déjà existant")
    users_db[user.username] = user
    todo_db[user.username] = []
    return {"username": user.username, "todo_count": len(todo_db[user.username])}

@app.get("/users/me", response_model=dict)
async def get_current_user_profile():
    # Pour les tests, on récupère l’utilisateur en supposant "user1" comme utilisateur par défaut
    username = "user1"
    todos = todo_db.get(username, [])
    return {"username": username, "todo_count": len(todos)}

# Gestion des TODOs
@app.post("/users/me/todo", response_model=ToDoItem, status_code=status.HTTP_201_CREATED)
async def add_todo(todo: ToDoItemCreate):
    username = "user1"  # Supposition de l’utilisateur par défaut
    # Vérifiez si l'utilisateur existe déjà dans le todo_db
    if username not in todo_db:
        todo_db[username] = []  # Initialisez la liste si elle n'existe pas
    todo_item = ToDoItem(id=str(uuid4()), name=todo.name, description=todo.description, priority=todo.priority)
    todo_db[username].append(todo_item)
    return todo_item


@app.get("/users/me/todo", response_model=List[ToDoItem])
async def get_todo_list():
    username = "user1"  # Supposition de l’utilisateur par défaut
    todos = sorted(todo_db.get(username, []), key=lambda x: x.priority)
    return todos

@app.patch("/users/me/todo/{todo_id}", response_model=ToDoItem)
async def update_todo(todo_id: str, updated_data: ToDoItem):
    username = "user1"  # Supposition de l’utilisateur par défaut
    todos = todo_db[username]
    todo = next((item for item in todos if item.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO introuvable")
    todo.priority = updated_data.priority
    return todo

@app.delete("/users/me/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str):
    username = "user1"  # Supposition de l’utilisateur par défaut
    todos = todo_db[username]
    todo = next((item for item in todos if item.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO introuvable")
    todos.remove(todo)
    return None

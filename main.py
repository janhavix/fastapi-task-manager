from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str


tasks = []


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    db_task = models.TaskModel(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.TaskModel).all()

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        db.commit()
        return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "Task not found"}


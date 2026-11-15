# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# import models, schemas
# from database import engine, SessionLocal

# model.Base.metadata.create_all(bind = engine)

# app = FastAPI

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # CREATE
# @app.post("/tasks", response_model= schemas.TaskOut, status_code= 201)
# def create_task(task: schemas.TaskCreate,db: Session = Depends(get_db)):
#     new_task = model.Task(**task.model_dump())
#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)
#     return new_task

# # READ ALL
# @app.get("/tasks", response_model= List[schemas.TaskOut])
# def list_tasks(db: Session = Depends(get_db)):
#     return db.query(model.Task).all()

# # READ ONE
# @app.get("/tasks/{task_id}", response_model= schemas.TaskOut)
# def get_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(model.Task).filter(model.Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code = 404, detail = "taksk not found")
#     return task

# # Update
# @app.put("/tasks/{task_id}", response_model= schemas.TaskOut)
# def update_task(task_id: int, data: schemas.TaskCreate, db: Session=Depends(get_db)):
#     task = db.query(model.Task).filter(model.Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     for key, value in data.model_dump().items():
#         setattr(task, key, value)
#     db.commit()
#     db.refresh(task)
#     return task

# # Delete
# @app.delete("/tasks/{task_id}", status_code=204)
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(model.Task).filter(model.Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     db.delete(task)
#     db.commit()



from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "My Backend is running!"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/tasks", response_model=schemas.TaskOut, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Read all
@app.get("/tasks", response_model=List[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# Read one
@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update
@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, data: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in data.model_dump().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

# Delete
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
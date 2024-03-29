from fastapi import FastAPI, HTTPException, Path, Body
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()

tasks_db = {}
taskboard_db = {}

class Task(BaseModel):
    title: str
    dueDate: date
    status: str
    priority: str
    specialStatus: Optional[str] = None
    assigneeId: str
    recipientId: str
    description: str

class TaskBoard(BaseModel):
    name: str
    initiatorId: str

class Member(BaseModel):
    userId: str
    permission: str

@app.post("/api/taskboard/")
async def create_taskboard(taskboard: TaskBoard):
    taskboard_id = len(taskboard_db) + 1
    taskboard_db[taskboard_id] = taskboard.dict()
    return {"taskboardId": taskboard_id, **taskboard.dict()}

@app.post("/api/taskboard/{boardId}/tasks/")
async def create_task(boardId: int, task: Task):
    if boardId not in taskboard_db:
        raise HTTPException(status_code=404, detail="TaskBoard not found")
    task_id = len(tasks_db) + 1
    tasks_db[task_id] = task.dict()
    return {"taskId": task_id, **task.dict()}

@app.put("/api/taskboard/{boardId}/tasks/{taskId}/")
async def update_task(boardId: int, taskId: int, task: Task):
    if boardId not in taskboard_db or taskId not in tasks_db:
        raise HTTPException(status_code=404, detail="TaskBoard or Task not found")
    tasks_db[taskId] = task.dict()
    return {"taskId": taskId, **task.dict()}

@app.delete("/api/taskboard/{boardId}/tasks/{taskId}/")
async def delete_task(boardId: int, taskId: int):
    if boardId not in taskboard_db or taskId not in tasks_db:
        raise HTTPException(status_code=404, detail="TaskBoard or Task not found")
    del tasks_db[taskId]
    return {"detail": "Task deleted"}

@app.patch("/api/taskboard/{boardId}/tasks/{taskId}/move")
async def move_task(boardId: int, taskId: int, newStatus: str = Body(..., embed=True)):
    if boardId not in taskboard_db or taskId not in tasks_db:
        raise HTTPException(status_code=404, detail="TaskBoard or Task not found")
    tasks_db[taskId]['status'] = newStatus
    return {"taskId": taskId, "newStatus": newStatus}

@app.post("/api/taskboard/{boardId}/members/")
async def add_member(boardId: int, member: Member):
    return {"boardId": boardId, **member.dict()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
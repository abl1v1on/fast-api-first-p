from fastapi import APIRouter, Depends
from typing import Annotated, List

from schemas import TaskAdd
from repository import TaskRepository
from schemas import Task


router = APIRouter(
    prefix='/api',
    tags=['Таски']
)


@router.get('/tasks')
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {'tasks': tasks}


@router.post('/create-task')
async def create_new_task(task: Annotated[TaskAdd, Depends()]):
    await TaskRepository.add_one(task)
    return {'task': task}

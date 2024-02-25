from sqlalchemy import select
from database import new_session, TaskTable
from schemas import TaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(
                **task_dict
            )
            session.add(task)

            await session.flush()
            await session.commit()

            return task.id
    
    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            tasks = select(TaskTable)
            result = await session.execute(tasks)
            return result.scalars().all()
        
    @classmethod
    async def get_one(cls, task_id: int):
        async with new_session() as session:
            task = select(TaskTable).where(TaskTable.id == task_id)
            result = await session.execute(task)
            return result.scalar()
        
    
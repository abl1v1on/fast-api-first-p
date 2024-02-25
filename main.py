from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print('ON')
    yield
    print('OFF')


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

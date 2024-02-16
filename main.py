from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import delete_tables, create_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('DB cleared')
    await create_tables()
    print('DB ready for work')
    yield
    print('Shutdown')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


from fastapi import FastAPI
from routers import datas, users


app = FastAPI()
app.include_router(users.router, tags=['Users'])
app.include_router(datas.router, tags=['Data'])
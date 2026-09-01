from fastapi import FastAPI
from routers.productrouter import prouter

app = FastAPI()


app.include_router(prouter)


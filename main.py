from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import route_todo
from schemas import SuccessMsg

app = FastAPI()

# CORSの設定
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ルーターの追加
app.include_router(route_todo.router)

@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "Welcome to Fast API"}

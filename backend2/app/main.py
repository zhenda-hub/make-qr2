from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 使用内存存储示例数据
items = []

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def read_root():
    return {"message": "欢迎使用 FastAPI 后端服务"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/health")
def health_check():
    return {"status": "healthy"}

from fastapi import APIRouter
from fastapi import HTTPExeption
from typing import List
from modules.items.schema.schemas import Item 
from modules.items.routes.createItem import items

router = APIRouter()

@router.get("/items/", response_model=List[Item])
def get_items():
    return items

@router.get("/items/{item_id}", response_model=Item)
def get_items(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPExeption(status_code=404, detail="Item not found")
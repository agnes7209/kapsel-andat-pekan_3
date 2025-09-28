from fastapi import APIRouter
from fastapi import HTTPException
from modules.items.schema.schemas import Item 
from modules.items.routes.createItem import items

router = APIRouter()

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, update_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return update_item
    raise HTTPException(status_code=404, detail="Item not found")
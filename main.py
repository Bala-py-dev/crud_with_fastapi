from fastapi import FastAPI, HTTPException, Depends
from databases import Database
from models import SessionLocal, Item, ItemTbl

app = FastAPI()
db = SessionLocal()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    item = db.query(Item).filter(Item.item_id==item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return {"item_id": item.item_id, "q": item.q}

@app.post("/items/")
def create_item(item_id: int, q: str = None):
    db_news = Item(item_id=item_id, q=q)
    db.add(db_news)
    db.commit()
    db.close()
    return {"item_id": item_id, "q": q}



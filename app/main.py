from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import schemas, models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/urls", response_model=schemas.URL)
def create_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_db_url(db=db, url=url)

@app.get("/{short_key}")
def redirect_to_target_url(short_key: str):
    if short_key == "teste":
        return RedirectResponse(url="https://www.google.com")
    return {"detail": "URL não encontrada"}

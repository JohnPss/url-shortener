import secrets
from sqlalchemy.orm import Session

from . import models, schemas


def create_db_url(db: Session, url: schemas.URLCreate) -> models.URL:
    key = secrets.token_urlsafe(5)
    secret_key = secrets.token_urlsafe(12)

    db_url = models.URL(
        target_url=url.target_url,
        key=key,
        secret_key=secret_key
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url

import datetime as _dt
from sqlalchemy import (
    Column as _Column,
    Integer as _Integer,
    String as _String,
)



from .database import Base


class URL(Base):
    """
    Esta classe representa a tabela 'urls' no nosso banco de dados.
    O SQLAlchemy usará este modelo para criar a tabela e para
    interagir com ela (criar, ler, atualizar, deletar registros).
    """
    __tablename__ = "urls"
    id = _Column(_Integer, primary_key=True, index=True)
    key = _Column(_String, unique=True, index=True)
    secret_key = _Column(_String, unique=True, index=True)
    target_url = _Column(_String, index=True)


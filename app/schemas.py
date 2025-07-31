from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URLCreate(URLBase):
    pass

class URL(URLBase):
    key: str
    secret_key: str

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import Optional, List

class Blog(BaseModel):
    id: Optional[str]
    title: str
    content: str
    author: str
    tags: List[str] = []
    created_at: Optional[str]

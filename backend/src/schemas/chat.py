from pydantic import BaseModel, Field
from typing import List, Optional

class QueryRequest(BaseModel):
    question: str
    selected_text: Optional[str] = None

class Source(BaseModel):
    file_path: str
    chapter_title: Optional[str] = None
    section_heading: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source] = []

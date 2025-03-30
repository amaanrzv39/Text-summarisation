from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    min_length: int = 30
    max_length: int = 150
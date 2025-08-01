from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ItineraryRequest(BaseModel):
    days: int
    interests: List[str]
    budget: str
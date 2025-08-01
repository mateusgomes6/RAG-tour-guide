from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ItineraryRequest(BaseModel):
    days: int
    interests: List[str]
    budget: str

@app.post("/generate_itinerary")
async def generate_itinerary(request: ItineraryRequest):
    rag = TourismRAG(load_vector_db())
    itinerary = rag.generate_itinerary(
        request.days, 
        ", ".join(request.interests), 
        request.budget
    )
    return {"itinerary": itinerary}

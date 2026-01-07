from typing import List, Optional
from pydantic import BaseModel, ValidationError

class SwedishStocks(BaseModel):
    totalNumberOfHits: int = 0
    hits: List[str] = []

# Debugging example
try:
    # Simulate a response with missing fields
    response = {}
    stock_data = SwedishStocks(**response)
except ValidationError as e:
    print("Validation failed:", e)
    print("Response structure:", response)

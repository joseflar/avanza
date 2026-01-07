from typing import List
from pydantic import BaseModel


class StockItem(BaseModel):
    orderbookId: str
    name: str


class SwedishStocks(BaseModel):
    totalNumberOfHits: int
    hits: List[StockItem]

from typing import List, Union
from pydantic import BaseModel, Field


class StockItem(BaseModel):
    orderbookId: str
    name: str


class SwedishStocks(BaseModel):
    totalNumberOfOrderbooks: Union[int, str] = Field(alias="totalNumberOfOrderbooks")
    stocks: List[StockItem]

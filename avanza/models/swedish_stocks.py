from typing import List, Union
from pydantic import BaseModel


class StockItem(BaseModel):
    orderbookId: str
    name: str


class SwedishStocks(BaseModel):
    totalNumberOfOrderbooks: Union[int, str]
    stocks: List[StockItem]

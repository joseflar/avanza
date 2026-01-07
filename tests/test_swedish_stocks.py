import pytest
from models.swedish_stocks import SwedishStocks

def test_missing_fields():
    response = {}  # Simulate missing fields
    stock_data = SwedishStocks(**response)
    assert stock_data.totalNumberOfHits == 0
    assert stock_data.hits == []

def test_partial_fields():
    response = {"totalNumberOfHits": 10}  # Partial data
    stock_data = SwedishStocks(**response)
    assert stock_data.totalNumberOfHits == 10
    assert stock_data.hits == []

def test_full_fields():
    response = {"totalNumberOfHits": 15, "hits": ["StockA", "StockB"]}
    stock_data = SwedishStocks(**response)
    assert stock_data.totalNumberOfHits == 15
    assert stock_data.hits == ["StockA", "StockB"]

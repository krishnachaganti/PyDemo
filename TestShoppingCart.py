
import pytest
from unittest.mock import MagicMock
from ShoppingCart import ShoppingCart

lineCnt = 0

@pytest.fixture()
def shoppingCart():
    shoppingCart = ShoppingCart()
    shoppingCart.addItemPrice("a", 1)
    shoppingCart.addItemPrice("b", 2)
    return shoppingCart

def test_canCalculateTotal(shoppingCart):
    shoppingCart.addItem("a")
    assert shoppingCart.calculateTotal() == 1

def test_getCorrectTotalWithMultipleItems(shoppingCart):
    shoppingCart.addItem("a")
    shoppingCart.addItem("b")
    assert shoppingCart.calculateTotal() == 3

def test_canAddDiscountRule(shoppingCart):
    shoppingCart.addDiscount("a", 3, 2)

def test_canApplyDiscountRule(shoppingCart):
    shoppingCart.addDiscount("a", 3, 2)
    shoppingCart.addItem("a")
    shoppingCart.addItem("a")
    shoppingCart.addItem("a")
    assert shoppingCart.calculateTotal() == 2

def test_exceptionWithBadItem(shoppingCart):
    with pytest.raises(Exception):
        shoppingCart.addItem("c")

def test_verifyReadPricesFile(shoppingCart, monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["c 3"]
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    shoppingCart.readPricesFile("testfile")
    shoppingCart.addItem("c")
    result = shoppingCart.calculateTotal()
    mock_open.assert_called_once_with("testfile")
    assert result == 3


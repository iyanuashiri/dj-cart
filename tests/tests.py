import pytest

# Create your tests here.


@pytest.mark.django_db
def test_cart_model(cart, cartitem):
    assert cart.checked_out is True
    assert cart.cart_price() == 1000
    assert cart.count() == 1
    assert cart.serializable() == [{'product_id': 1, 'quantity': 10, 'price': 100.00}]


@pytest.mark.django_db
def test_cart_item_model(cartitem, cart):
    assert cartitem.cart == cart
    assert cartitem.quantity == 10
    assert cartitem.price == 100.00
    assert cartitem.total_price == 1000




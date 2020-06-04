from pytest_factoryboy import register

from .factories import CartFactory, CartItemFactory, UserFactory


register(UserFactory, 'user')
register(CartFactory, 'cart')
register(CartItemFactory, 'cartitem')

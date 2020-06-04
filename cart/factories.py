from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
import factory

from .models import CartItem, Cart


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = 'test1@yahoo.com'
    email = 'test1@yahoo.com'
    first_name = 'Iyanuoluwa'
    last_name = 'Ajao'
    password = factory.PostGenerationMethodCall('set_password', 'olukayss')

    is_superuser = True
    is_staff = True
    is_active = True


class CartFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory, cart=None)
    checked_out = True

    class Meta:
        model = Cart


class CartItemFactory(factory.DjangoModelFactory):
    cart = factory.SubFactory(CartFactory)
    quantity = 10
    price = 100.00
    product_object_id = factory.SelfAttribute('product.id')
    product_content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.product))
    product = factory.SubFactory(UserFactory)

    class Meta:
        exclude = ['product']
        model = CartItem


# dj-cart

## Introduction

This is not a session based cart system. This implementation stores the contents of the cart in the database.

## Prerequisites

- Django 1.1+
- django content type framework in your INSTALLED_APPS


## Installation

```bash
pip install dj-cart
```

After installation is complete:

    add 'cart' to your INSTALLED_APPS 
    
 Run
 
 ```bash
 python manage.py migrate
 ```

## Usage



```python
from cart.models import Cart
from myproducts.models import Product


class CartAdd(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request, product_id):
        quantity = request.data.get('quantity')
        product = self.get_object(product_id)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart.add_item(product, product.price, quantity)
        return Response(status=status.HTTP_201_CREATED)


class CartRemove(APIView):
      def get_object(self, product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, product_id):
        product = self.get_object(product_id)
        cart = get_object_or_404(Cart, user=self.request.user)
        cart.remove_item(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetail(APIView):

    def get(self, request):
        try:
            cart = Cart.objects.get(patient=self.request.user.patient)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(patient=self.request.user.patient)
        return Response(cart.serializable(), status=status.HTTP_200_OK)

```


## Testing

```bash
pytest
```

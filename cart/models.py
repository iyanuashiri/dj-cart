from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('cart_user'),
                                primary_key=True)
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')

    def __str__(self):
        return self.created_at

    def add_item(self, product, unit_price, quantity=1):
        product_content_type = ContentType.objects.get_for_model(product)
        item = self.cart_items.filter(cart=self, product_content_type=product_content_type,
                                      product_object_id=product.pk).first()
        if item:
            item.unit_price = unit_price
            item.quantity += int(quantity)
            item.save()
        else:
            return CartItem.objects.create(cart=self, quantity=quantity, unit_price=unit_price,
                                           product_content_type=product_content_type, product_object_id=product.pk)

    def remove_item(self, product):
        product_content_type = ContentType.objects.get_for_model(product)
        item = self.cart_items.filter(cart=self, product_content_type=product_content_type,
                                      product_object_id=product.pk).first()
        if item:
            item.delete()

    def clear(self):
        self.cart_items.all().delete()

    def cart_price(self):
        return sum(item.total_price for item in self.cart_items.all())

    def count(self):
        return self.cart_items.all().count()

    def serializable(self):
        data = []
        for item in self.cart_items.all():
            item_id = str(item.product)
            item_dict = {
                    'product_id': item.product.pk,
                    'unit_price': item.unit_price,
                    'quantity': item.quantity,
                }
            data.append(item_dict)
        return data


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'), related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    product_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    product_object_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_content_type', 'product_object_id', )

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __str__(self):
        return f'{self.quantity} units of {self.product.__class__.__name__}'

    @property
    def total_price(self):
        return self.quantity * self.price

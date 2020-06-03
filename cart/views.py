from django.shortcuts import render

# Create your views here.


class CartAdd(APIView):
    """
    This endpoint is for adding an item to dj_cart

    :param pk: Product primary key

    :data quantity: quantity to be ordered. IntegerField
    """
    def get_object(self, product_id):
        try:
            return PharmacyProducts.objects.get(pk=product_id)
        except PharmacyProducts.DoesNotExist:
            raise Http404

    def post(self, request, product_id):
        quantity = request.data.get('quantity')
        product = self.get_object(product_id)
        cart, created = Cart.objects.get_or_create(patient=self.request.user.patient)
        if created:
            cart.add_item(product, product.get_dro_price, quantity)
        else:
            cart.add_item(product, product.get_dro_price, quantity)
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)


class CartRemove(APIView):
    """
    :param pk: Product primary key

    This endpoint is for removing an item from dj_cart
    """

    def get_object(self, product_id):
        try:
            return PharmacyProducts.objects.get(pk=product_id)
        except PharmacyProducts.DoesNotExist:
            raise Http404

    def put(self, request, product_id):
        product = self.get_object(product_id)
        cart = get_object_or_404(Cart, patient=self.request.user.patient)
        cart.remove_item(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetail(APIView):
    """
    This endpoint is to view the details of a dj_cart
    """
    def get(self, request):
        try:
            cart = Cart.objects.get(patient=self.request.user.patient)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(patient=self.request.user.patient)
        return Response(cart.cart_serializable(), status=status.HTTP_200_OK)

from django.conf.urls import url, include
# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from crud.models import Product, Like, Order, DeliveryType
import os, json, logging, datetime, shutil, zipfile
logger = logging.getLogger(__name__)
from rest_framework.decorators import detail_route
from rest_framework import decorators
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK
from rest_framework.request import Request
from rest_framework.response import Response

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'username')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image','description', 'price', 'currency', 'category_id', 'likes')

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'product_id', 'user_id')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product_id', 'user_id', 'delivery_id', 'product_count', 'total_price')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        query_set = super(UserViewSet, self).get_queryset()
       	logger.error(json.dumps(self.request.query_params))
        return query_set

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query_set = super(ProductViewSet, self).get_queryset()
       	logger.error(json.dumps(self.request.query_params))
       	logger.error(self.action)
       	if 'action' in self.request.query_params:
       		if self.request.query_params['action'] == 'category': 
       			if 'category' in self.request.query_params:
       				category = self.request.query_params['category']
       				query_set = query_set.filter(category_id = category)
        # if 'action' in self.request.query_params: 
        	if self.request.query_params['action'] == 'title':
        		if 'title' in self.request.query_params:
        			title = self.request.query_params['title']
        			query_set = query_set.filter(title = title)

        return query_set

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @detail_route(methods=['post'])
    def finish(self, request: Request, pk: int = None) -> Response:
        return Response(status=HTTP_200_OK)

    # def get_queryset(self):
    #     query_set = super(OrderViewSet, self).get_queryset()
    #    	logger.error(json.dumps(self.request.query_params))
    #    	logger.error(self.action)
    #    	if 'action' in self.request.query_params:
    #    		if self.request.query_params['action'] == 'create': 
    #    			logger.error(self.request.GET['delivery_id'])
    #     return query_set

    def get_queryset(self):
        query_set = super(OrderViewSet, self).get_queryset()
      
       	logger.error(self.action)
       	if 'action' in self.request.query_params and  self.request.query_params['action'] == 'create':
       		logger.error(self.request.GET['delivery_id'])
       		logger.error(self.request.GET['delivery_id'])
       		logger.error(self.request.GET['delivery_id'])
       		product = Product.objects.get(id=self.request.GET['product_id'])
       		user = User.objects.get(id=self.request.GET['user_id'])
       		delivery = DeliveryType.objects.get(id=self.request.GET['delivery_id'])

       		product_count = int(self.request.GET['product_count'])
       		product_price = int(product.price)
       		delivery_price = int(delivery.price)

       		if delivery.fixed == 'TRUE':
       			total_price = product_price*product_count + delivery_price
       		else:
       			total_price = product_price*product_count+ (product_price*product_count*delivery_price/100)

       		order = Order(product=product, user=user, delivery= delivery, product_count = product_count, total_price = total_price)
       		order.save()

       	
        return query_set

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'orders', OrderViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = router.urls

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
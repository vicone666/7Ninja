from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'user$', views.showUser, name='showUser'),
    url(r'user/create$', views.createUser, name='createUser'),
    url(r'user/edit/(?P<id>\d+)$', views.editUser, name='editUser'),
    url(r'user/edit/update/(?P<id>\d+)$', views.updateUser, name='updateUser'),
    url(r'user/delete/(?P<id>\d+)$', views.deleteUser, name='deleteUser'),

    url(r'product$', views.showProduct, name='showProduct'),
    url(r'product/create$', views.createProduct, name='createProduct'),
    url(r'product/edit/(?P<id>\d+)$', views.editProduct, name='editProduct'),
    url(r'product/edit/update/(?P<id>\d+)$', views.updateProduct, name='updateProduct'),
    url(r'product/delete/(?P<id>\d+)$', views.deleteProduct, name='deleteProduct'),


    url(r'category$', views.showCategory, name='showCategory'),
    url(r'category/create$', views.createCategory, name='createCategory'),
    url(r'category/edit/(?P<id>\d+)$', views.editCategory, name='editCategory'),
    url(r'category/edit/update/(?P<id>\d+)$', views.updateCategory, name='updateCategory'),
    url(r'category/delete/(?P<id>\d+)$', views.deleteCategory, name='deleteCategory'),

    url(r'order$', views.showOrder, name='showOrder'),
    url(r'order/create$', views.createOrder, name='createOrder'),
    url(r'order/edit/(?P<id>\d+)$', views.editOrder, name='editOrder'),
    url(r'order/edit/update/(?P<id>\d+)$', views.updateOrder, name='updateOrder'),
    url(r'order/delete/(?P<id>\d+)$', views.deleteOrder, name='deleteOrder'),


    url(r'delivery$', views.showDelivery, name='showDelivery'),
    url(r'delivery/create$', views.createDelivery, name='createDelivery'),
    url(r'delivery/edit/(?P<id>\d+)$', views.editDelivery, name='editDelivery'),
    url(r'delivery/edit/update/(?P<id>\d+)$', views.updateDelivery, name='updateDelivery'),
    url(r'delivery/delete/(?P<id>\d+)$', views.deleteDelivery, name='deleteDelivery'),

]
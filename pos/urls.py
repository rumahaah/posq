from django.urls import path, include
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'orders', views.OrderViewSet)
# router.register(r'orderitems', views.OrderItemViewSet)


urlpatterns = [
    path('', views.pos_order, name='pos_order'),
    # path('', include(router.urls)),
    path('getorder', views.getorder, name='getorder'),
    path('cobaorder', views.cobaorder, name='cobaorder'),
    path('reportorder', views.reportorder, name='reportorder'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
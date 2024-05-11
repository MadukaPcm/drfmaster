from django.urls import path
from django.contrib import admin
from core import views as core_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from ecommerce import views as ecommerce_views


router = routers.DefaultRouter()

router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')
 
 
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('token/', obtain_auth_token),
] 
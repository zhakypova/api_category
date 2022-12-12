
from django.contrib import admin
from django.urls import path, include
from onlineshop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('category', views.CategoryViewSet)
router.register('item', views.ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

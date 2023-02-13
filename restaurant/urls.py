from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
from djoser import views as djoser_views 


router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename="menu-item"),
router.register(r'users', djoser_views.UserViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path("", include('djoser.urls.jwt')),
]
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
from djoser import views as djoser_views 


router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename="menu-item"),
# router.register(r'users', djoser_views.UserViewSet),
# router.register(r'jwt', djoser_jwt.)

urlpatterns = [
    path('', include(router.urls)),
    # re_path(r'^api/', include('djoser.urls')),
    # re_path("", include('djoser.urls.jwt')),
]
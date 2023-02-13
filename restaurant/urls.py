from django.urls import path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('menu-items', MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
]


from django.urls import path

from .views import ItemCreate, ItemDelete, ItemList, ItemUpdate

urlpatterns = [
    path("", ItemList.as_view(), name="item-list"),
    path("add/", ItemCreate.as_view(), name="item-create"),
    path("<pk>/", ItemUpdate.as_view(), name="item-update"),
    path("<pk>/delete/", ItemDelete.as_view(), name="item-delete"),
]

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Item


class ItemCreate(CreateView):
    model = Item
    fields = "__all__"
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("item-list")


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy("item-list")


class ItemList(ListView):
    paginate_by = 10

    def get_queryset(self):
        if "q" in self.request.GET:
            queryset = Item.objects.filter(description__icontains=self.request.GET["q"])
            return queryset.order_by("description")

        return Item.objects.order_by("description")


class ItemUpdate(UpdateView):
    model = Item
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("item-list")

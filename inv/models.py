from django.db.models import CharField, FloatField, Model, PositiveIntegerField
from django.urls import reverse


class Item(Model):
    description = CharField(max_length=100)
    qty = PositiveIntegerField(default=0)
    cost = FloatField(default=0)
    price = FloatField(default=0)

    def __str__(self):
        return str(self.description)

    def get_absolute_url(self):
        return reverse("item-update", kwargs={"pk": self.pk})

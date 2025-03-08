
from django.db import models


class Tag(models.Model):

    id = models.CharField(null=False, primary_key=True, max_length=20)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=10)

    def __str__(self):
        return f"Etiqueta: {self.name}, id: {self.id}"

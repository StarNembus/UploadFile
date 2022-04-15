from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'

from django.db import models


class Home(models.Model):
    name  = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
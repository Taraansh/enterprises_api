from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
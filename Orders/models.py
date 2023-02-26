from django.db import models
import uuid

# Create your models here.
class Representative(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(blank=True, null = True)
    address = models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4(),primary_key=True, unique=True)



    def __str__(self):
        return self.name


class Customer(models.Model):
    rep_name = models.ForeignKey(Representative, null=True, blank=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    products_data = models.TextField(blank=True, null=True)
    pk_id=models.UUIDField(default=uuid.uuid4, primary_key=True)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



    



    
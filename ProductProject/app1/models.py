from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,unique=True)
    product_quantity=models.IntegerField(default=0)
    product_price=models.FloatField(null=False)


    def __str__(self):
        return self.product_id

    def __str__(self):
        return self.product_name



class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    product=models.ManyToManyField(Product)
    user_name=models.CharField(max_length=100)

    def __str__(self):
        return self.user_id

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    statte=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    date_ordered=models.DateTimeField(auto_now_add=True)
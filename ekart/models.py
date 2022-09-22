from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Categary(models.Model):
    categary_name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.categary_name

class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    price =models.PositiveIntegerField()
    image=models.ImageField(null=True)
    categary=models.ForeignKey(Categary,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart")
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class meta:
        unieque_together=("user","product")
# Create your models here.

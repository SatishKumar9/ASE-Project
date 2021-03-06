from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MaxValueValidator
from Restaurants.models import Restaurant, FoodCategory, Food
# from Delivery.models import Delivery
# Create your models here.


class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Customer_Fname = models.CharField(max_length=250)
    Customer_Lname = models.CharField(max_length=250)
    Customer_Regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                    message="Phone number must be entered in the format:" +
                                            " '+999999999'. Up to 15 digits allowed.")
    Customer_Num = models.CharField(validators=[Customer_Regex], max_length=17)
    Customer_Pic = models.ImageField(upload_to='Customers/Pictures/Profiles')
    Customer_Email = models.EmailField()


class Address(models.Model):
    Address_ID = models.AutoField(primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Home = models.CharField(max_length=250)
    Society = models.CharField(max_length=250)
    Area = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    State = models.CharField(max_length=250)
    Pin = models.CharField(max_length=6, default=000000)


class Order(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Order_Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Order_Restaurant_ID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Order_Status = models.IntegerField(MaxValueValidator(5))
    Order_Time = models.DateTimeField(default=timezone.now)
    # Order_Discount =
    # Order_Total_Price =


class Item(models.Model):
    Item_ID = models.AutoField(primary_key=True)
    Item_Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Item_Food_ID = models.ForeignKey(Food, on_delete=models.CASCADE)
    Item_Quantity = models.IntegerField(MaxValueValidator(10))
    # Item_Price =

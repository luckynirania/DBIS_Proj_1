from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import student, manager
from djmoney.models.fields import MoneyField
# Create your models here.

class feedback(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    response = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class staff(models.Model):
    staff_id = models.CharField(max_length = 50,primary_key=True)
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    address = models.TextField()
    contact = models.CharField(max_length = 15)
    salary = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    acc_no = models.CharField(max_length = 50)
    bank_name = models.CharField(max_length = 50)
    IFSC = models.CharField(max_length = 50)
    # manager = models.OneToOneField(manager,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class item(models.Model):
#     item_id = models.CharField(max_length=25,primary_key=True)
#     name = models.CharField(max_length=25)
#     critical_quantity = models.IntegerField()
#     item_unit = models.CharField(max_length=5)

#     def __str__(self):
#         return self.item_id

class inventory(models.Model):
    item_id = models.CharField(max_length=25,primary_key=True)
    name = models.CharField(max_length=25)
    critical_quantity = models.IntegerField()
    item_unit = models.CharField(max_length=5)
    quantity = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class supplier(models.Model):
    sup_id = models.CharField(max_length=25,primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class bill(models.Model):
    bill_id = models.CharField(max_length=25,primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    paid = models.BooleanField()
    # date_paid = models.DateTimeField(default=None,blank=True)

    def __str__(self):
        return self.bill_id

class purchase(models.Model):
    pur_id = models.CharField(max_length=25,primary_key=True)
    sup_id = models.ForeignKey(supplier,on_delete=models.CASCADE)
    bill_id = models.ForeignKey(bill,on_delete=models.CASCADE)
    item_id = models.ForeignKey(inventory,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=25)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')

    def __str__(self):
        return self.pur_id

class consumption(models.Model):
    item_id = models.ForeignKey(inventory,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item_id

class expenses(models.Model):
    date = models.DateTimeField(default=timezone.now)
    amount = MoneyField(max_digits=5, decimal_places=2, default_currency='INR')

    def __str__(self):
        return self.date

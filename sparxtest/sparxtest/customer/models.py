from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    account_no = models.CharField(max_length=30, blank=True)

# Create your models here.
class TransactionUser(models.Model):
	AMT_STATUS = (
	("Deposit",'Deposit'),
	("Withdraw",'Withdraw'),
	)
	name  = models.CharField(max_length=100)
	account_no  = models.CharField(max_length=30, blank=True)
	user_id = models.IntegerField(blank=True, null=True)
	amount = models.IntegerField(blank=True, null=True)
	status = models.CharField(blank=True,null=True,max_length=100,choices=AMT_STATUS)
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created On',null=True,blank=True)
	updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
	c=[
		('0','Guest'),
		('1','Customer'),
		('2','SalesPerson'),
		('3','bidder'),
	]
	
	role_type = models.CharField(max_length=5,choices=c,default='0')
	uid=models.CharField(max_length=15)

	
class AntiqueItem(models.Model):
    y=[
         ('Antique','Antique'),
         ('Arts','Arts'),
         ('HandiCrafts','HandiCrafts'),
         ('Jewelry','Jewelry'),
    ]
    name = models.CharField(max_length=200)
    TagLine= models.CharField(max_length=200,default='')
    description = models.TextField()
    image = models.ImageField(null=True,upload_to='antiques/')
    startingprice = models.PositiveIntegerField(default=200)
    maximumprice = models.PositiveIntegerField(default=600)
    itemtype=models.CharField(max_length=100,default='0',choices=y)
    usitem=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

class Auction(models.Model):
    item = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    bid_amount = models.PositiveIntegerField(default=200)
    highest_bid = models.PositiveIntegerField(default=500, null=True, blank=True)
    winner_name=models.CharField(max_length=200,default='')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


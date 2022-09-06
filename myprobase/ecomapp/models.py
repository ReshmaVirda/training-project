from distutils.command.upload import upload
from django.db import models



# Create your models here.
class account(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    pass1 = models.CharField(max_length=200)
    pass2 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    ques_CHOICES = (
        ('WHICH TOWN DO U LIVE IN','which town do u live in'),
        ('HOBBY','hobby'),
        ('SPORTS','sports'),
    )
    questype = models.CharField(max_length=200,choices=ques_CHOICES,default='WHICH TOWN DO U LIVE IN')
    

    def __str__(self):
        return self.username

class product(models.Model):
    productname = models.CharField(max_length=200)
    productprice = models.IntegerField(default=0)
    productdesc = models.CharField(max_length=200)
    productimage = models.ImageField(upload_to = 'proimage/',blank=True)

    def __str__(self):
        return self.productname

class cart(models.Model):
    useofcart = models.ForeignKey(account,on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=200)
    pro_price = models.IntegerField(default=0)
    pro_desc = models.CharField(max_length=200)
    pro_image = models.CharField(max_length=200)
    pro_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.pro_name
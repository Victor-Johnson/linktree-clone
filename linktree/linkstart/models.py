from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    BG_CHOICES =(
        ('blue','Blue'),
        ('green','Green'),
        ('red','Red'),
        ('purple','Purple'),
        ('yellow','Yellow'),
        ('black','Black'),
    )

    Name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    profile_pictures = models.ImageField(upload_to='images/profileshots')
    bg_color = models.CharField(max_length=50,choices=BG_CHOICES)
    
    def ___str___(self):
        return self.name


class Link(models.Model):
    #text,url,profile
    text = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="link")




class Shop(models.Model):
    #title, price, description, Rating, Review,link
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    


# class Rating(models.Model):
#     RATING_CHOICES = [
#         (1, '1 - Poor'),
#         (2, '2 - Fair'),
#         (3, '3 - Good'),
#         (4, '4 - Very Good'),
#         (5, '5 - Excellent'),
#     ]

#     product = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='ratings')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     comment = models.TextField(blank=True, null=True)  # Optional field for user comments
#     created_at = models.DateTimeField(auto_now_add=True)



# class Appointment_Table(models.Model):
#     #Type of appointment , price , Date input ,description 

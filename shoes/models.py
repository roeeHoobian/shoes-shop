from django.db import models
from django.contrib.auth.models import User

class Shoe(models.Model):
    CATEGORY_CHOICES = [
        ('sneakers', 'Sneakers'),
        ('boots', 'Boots'),
        ('sandals', 'Sandals'),
        ('formal', 'Formal'),
        ('sports', 'Sports'),
    ]

    name = models.CharField(max_length=255)  # Shoe name or model
    brand = models.CharField(max_length=100)  # Brand of the shoe
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='sneakers'
    )  # Shoe category
    description = models.TextField(blank=True, null=True)  # Description of the shoe
    size = models.FloatField(blank=True, null=True)  # Shoe size
    color = models.CharField(max_length=50, blank=True, null=True)  # Primary color(s)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the shoe
    stock_quantity = models.IntegerField(default=0)  # Stock quantity
    release_date = models.DateField(blank=True, null=True)  # Release date of the shoe
    is_active = models.BooleanField(default=True)  # Active or discontinued
    image  = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"



class Review(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.shoe.name} ({self.rating}/5)"


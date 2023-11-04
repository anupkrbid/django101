from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(60)])

    def __str__(self):
        return f"{self.name}({self.email}) - {self.age}"

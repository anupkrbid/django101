from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(60)])
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.name}({self.email}) - {self.age} - {self.slug}"

    def save(self, *args, **kwargs):
        # self.slug = slugify(f"{self.name} {self.id}") # id not present before save
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("specific-user-path-id", kwargs={"pk": self.pk})
        # return reverse("specific-user-path-id", args=[self.id])
        return reverse("specific-user-path-slug", args=[self.slug])

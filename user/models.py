from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Access(models.Model):
    type = models.TextField()

    def __str__(self):
        return f"{self.type}"

    class Meta:
        verbose_name_plural = "Access"


class Passport(models.Model):
    number = models.IntegerField(
        validators=[MaxValueValidator(9999999999999999)])

    def __str__(self):
        return f"{self.number}"


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(60)])
    access = models.ManyToManyField(Access, related_name="users")
    passport = models.OneToOneField(
        Passport, on_delete=models.CASCADE, related_name="user", null=True)
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.age} - {self.slug}"

    # def save(self, *args, **kwargs):
    #     # self.slug = slugify(f"{self.name} {self.id}") # id not present before save
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("specific-user-path-id", kwargs={"pk": self.pk})
        # return reverse("specific-user-path-id", args=[self.id])
        return reverse("specific-user-path-slug", args=[self.slug])


class PhoneNo(models.Model):
    country_code = models.CharField(max_length=3)
    number = models.IntegerField(
        validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="phone_nos")

    def __str__(self):
        return f"{self.country_code} ({self.number}) - {self.user.name}"

    class Meta:
        verbose_name_plural = "Phone Nos"

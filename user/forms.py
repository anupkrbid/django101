from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="User's name", max_length=50, widget=forms.Textarea, error_messages={
        "required": "User's name must not be empty",
        "max_length": "Please enter a shorter name"
    })
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18, max_value=60)
    access = forms.SelectMultiple()
    passport = forms.IntegerField()

    # name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    # age = models.IntegerField(
    #     validators=[MinValueValidator(18), MaxValueValidator(60)])
    # access = models.ManyToManyField(Access, related_name="users")
    # passport = models.OneToOneField(
    #     Passport, on_delete=models.CASCADE, related_name="user", null=True)
    # slug = models.SlugField(default="", null=False, db_index=True)

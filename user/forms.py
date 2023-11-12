from django import forms
from .models import User


# class UserForm(forms.Form):
#     name = forms.CharField(label="User's name", max_length=50, widget=forms.Textarea, error_messages={
#         "required": "User's name must not be empty",
#         "max_length": "Please enter a shorter name"
#     })
#     email = forms.EmailField()
#     age = forms.IntegerField(min_value=18, max_value=60)
#     access = forms.CharField(widget=forms.Select,
#                              choices=[("READ", "READ"), ("READ", "UPDATE"), ("READ", "DELETE")])
#     passport = forms.IntegerField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ["name", "email", "age", "access", "passport"]
        # fields = "__all__"
        exclude = ["slug"]
        labels = {
            "name": "User's Name",
            "email": "User's Email",
            "age": "User's Age",
            "Access": "User's Access",
            "Passport": "User's Passport"
        }
        error_messages = {
            "name": {
                "requierd": "User's name is required!",
                "max_length": "Please enter a shorter name"
            }
        }

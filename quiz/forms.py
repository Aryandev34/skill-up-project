from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

_field = {"class": "su-input"}


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs=_field),
            "email": forms.EmailInput(attrs=_field),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(_field)
        self.fields["password2"].widget.attrs.update(_field)

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator
)

from taxi.models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    CHARACTERS = 8

    class Meta:
        model = Driver
        fields = ("license_number",)

    license_number = forms.CharField(
        required=True,
        validators=[
            MinLengthValidator(CHARACTERS),
            MaxLengthValidator(CHARACTERS),
            RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message=(
                    "There must be exactly 8 characters:"
                    "the first 3 are uppercase letters,"
                    "the last 5 are numbers."
                )
            ),
        ]
    )


class CarCreateForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"

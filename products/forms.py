from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Product, Profile
from django.contrib.auth import login, authenticate

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
        help_texts = {
            'username': '',
        }

class ProfileForm(forms.ModelForm):
    city = forms.CharField(max_length=30, required=True)
    adress = forms.CharField(max_length=30, required=True , widget=forms.TextInput(attrs={'placeholder': 'abcstreet 12'}))
    ZIP_code = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': '1234AB'}))

    class Meta:
        model = Profile
        fields =('city', 'adress', 'ZIP_code')

class SignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=30, required=False)
        last_name = forms.CharField(max_length=30, required=False)
        email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'example@example.com'}))
        city = forms.CharField(max_length=30, required=True)
        adress = forms.CharField(max_length=30, required=True , widget=forms.TextInput(attrs={'placeholder': 'abcstreet 12'}))
        ZIP_code = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': '1234AB'}))

        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', 'city', 'adress', 'ZIP_code', 'username', 'password1', 'password2')

class CartClothAddForm(forms.Form):

    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 16)]
    PRODUCT_SIZE_CHOICES = [(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')]

    size = forms.TypedChoiceField(choices = PRODUCT_SIZE_CHOICES, coerce=int)
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class CartShoeAddForm(forms.Form):

    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 16)]
    PRODUCT_SIZE_CHOICES = [((i-29), str(i) + " EU") for i in range (35, 49)]

    size = forms.TypedChoiceField(choices = PRODUCT_SIZE_CHOICES, coerce=int)
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class CheckOutForm(forms.Form):
    clicked = forms.BooleanField(initial=True, widget=forms.HiddenInput)

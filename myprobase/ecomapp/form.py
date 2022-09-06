from pyexpat import model
from django import forms
from django.db import models
from django.forms import fields

from ecomapp.models import account, cart, product

class accountform(forms.ModelForm):

    class Meta:

        model = account
        fields = '__all__'

class proform(forms.ModelForm):

    class Meta:

        model = product
        fields = '__all__'

class cartform(forms.ModelForm):

    class Meta:

        model = cart
        fields = '__all__'


from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget
from django.utils import timezone

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['crust', 'cheese', 'sauce', 'size',
                  'Chicken', 'Pepperoni', 'Mushroom', 
                  'Olives', 'Ham', 'Pineapple', 
                  'Pesto', 'Jalapeno', 'Onion',
                  'Peppers', 'Anchovies', 'Sweetcorn']
        
    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        self.fields['crust'].queryset = Crust.objects.all()
        self.fields['cheese'].queryset = Cheese.objects.all()
        self.fields['sauce'].queryset = Sauce.objects.all()
        self.fields['size'].queryset = Size.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['cheese', 'sauce', 'size', 'crust']:
            field_value = cleaned_data.get(field_name)
            if '-' in str(field_value):
                raise forms.ValidationError("Please fill out all fields.")
        return cleaned_data
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'card_number', 'card_expiry', 'card_cvv']

        widgets = {
            'card_expiry': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name cannot contain numbers.")
        return name

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if not card_number.isdigit() or len(card_number) != 16:
            raise forms.ValidationError("Card number must be 16 digits.")
        return card_number

    def clean_card_expiry(self):
        card_expiry = self.cleaned_data['card_expiry']
        if card_expiry < timezone.now():
            raise forms.ValidationError("Card expiry date cannot be in the past.")
        return card_expiry

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data['card_cvv']
        if len(card_cvv) != 3 or not card_cvv.isdigit():
            raise forms.ValidationError("Please enter a valid 3 digit CVV.")
        return card_cvv

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

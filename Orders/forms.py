from .models import Representative
from .models import Customer
from django.forms import ModelForm
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email", "delivery_address", "products_data"]

        widgets ={
            "name":forms.Textarea(attrs={'class': 'input', "rows":1,"cols":40}),
            "phone":forms.Textarea(attrs={'class': 'input', "rows":1,"cols":40}),
            "email":forms.Textarea(attrs={'class': 'input', "rows":1,"cols":40}),
            "delivery_address":forms.Textarea(attrs={"rows":5,"cols":40,'class': 'input'}),
            "products_data":forms.Textarea(attrs={'class': 'input',"rows":20,"cols":40}),

        }

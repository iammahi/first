from django import forms
from .models import *
# our new form
"""class UpdateForm(forms.ModelForm):
    class Meta:
        model = ConForm_Orders
        fields = ('__all__')
        exclude =['json']"""
class UpdateForm(forms.ModelForm):
    class Meta:
        model = ConForm_Orders
        fields= ['status','delivery_boy_id']
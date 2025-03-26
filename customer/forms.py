from django import forms
from django.contrib.auth.models import User
from insurance.models import Claim
from . import models
from .models import Claim


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']
        
class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ["policy_number", "claim_reason", "claim_amount", "supporting_document"]

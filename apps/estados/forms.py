from django import forms

from .models import Estado as Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

from django import forms

from .models import Fundo as Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

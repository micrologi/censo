from django import forms

from .models import EstadoCivil as Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

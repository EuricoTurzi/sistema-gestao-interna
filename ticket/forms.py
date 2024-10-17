from django import forms
from django.forms import inlineformset_factory
from .models import ticketmodel

class ticketForm(forms.ModelForm):
    class Meta:
        model = ticketmodel
        fields = ['setor', 'erro', 'correcao']
        widgets = {
           
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'erro': forms.Textarea(attrs={'class': 'form-control'}),
            'correcao': forms.Textarea(attrs={'class': 'form-control'}),
           
        }

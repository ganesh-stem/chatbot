from django import forms
from .models import SA


class SAForm(forms.ModelForm):
    input_sentence  =   forms.CharField(label='', 
                                widget=forms.TextInput(attrs={
                                    "placeholder": "Enter the Sentence",
                                    'id': 'TA1',
                                    'name': 'msg',
                                    'class': 'msger-input' }))
    

    class Meta:
        model = SA
        fields = [
            'input_sentence',
        ]


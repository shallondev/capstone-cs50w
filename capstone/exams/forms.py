from django.forms import ModelForm
from django import forms

from .models import Exam

class CreateExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            'size', 'time'
        ]
        widgets = {
            'size': forms.NumberInput(attrs={'class': 'form-control form-control-small', 'placeholder': 'Number of Questions (default=30) (1-30)'}),
            'time': forms.NumberInput(attrs={'class': 'form-control form-control-small', 'placeholder': 'Enter time in minutes (default=180) (range: (5, 180))'}),
        }
        labels = {
            'size': 'Number of Questions',
            'time': 'Time in Minutes',
        }
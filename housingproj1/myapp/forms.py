from django import forms
from .models import Contribution, ExpenseDetail

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'  # Define the desired date format

class ContributionForm(forms.ModelForm):
    date = forms.DateField(widget=CustomDateInput)  # Apply the custom widget

    class Meta:
        model = Contribution
        fields = '__all__'

class ExpenseDetailForm(forms.ModelForm):
    date = forms.DateField(widget=CustomDateInput)  # Apply the custom widget

    class Meta:
        model = ExpenseDetail
        fields = '__all__'

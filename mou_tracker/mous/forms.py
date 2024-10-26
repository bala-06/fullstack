# mous/forms.py
from django import forms
from .models import Department, Organization, Outcome

class MOUFilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, label="Department")
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(), required=False, label="Organization")
    outcome = forms.ModelChoiceField(queryset=Outcome.objects.all(), required=False, label="Outcome")
    status = forms.ChoiceField(choices=[('', 'All'), ('active', 'Active'), ('expired', 'Expired')], required=False, label="Status")

# mous/forms.py
from django import forms
from .models import MOU

class MOUUploadForm(forms.ModelForm):
    class Meta:
        model = MOU
        fields = ['title', 'department', 'organization', 'outcomes', 'start_date', 'end_date', 'pdf_file']
        widgets = {
            'department': forms.SelectMultiple(attrs={'size': 6}),
            'outcomes': forms.SelectMultiple(attrs={'size': 6}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'MoU Title',
            'department': 'Departments',
            'organization': 'Organization',
            'outcomes': 'Outcomes',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'pdf_file': 'Upload MoU PDF'
        }

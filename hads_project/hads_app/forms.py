# hads_app/forms.py

from django import forms
from .models import HADSQuestion, SubjectiveQuestion

class HADSQuestionAdminForm(forms.ModelForm):
    class Meta:
        model = HADSQuestion
        exclude = ('weight_0', 'weight_1', 'weight_2', 'weight_3')

class SubjectiveQuestionForm(forms.ModelForm):
    class Meta:
        model = SubjectiveQuestion
        fields = '__all__'

from django import forms
from .models import Course


# class NameForm(forms.Form):
#     name = forms.CharField(label='Course name', max_length=100)
#     st_date = forms.DateField(label='Start date')
#prof_name = forms.CharField(widget=forms.Textarea())

class NameForm (forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'st_date']
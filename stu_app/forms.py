from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = ('name', 'dob', 'physics', "chemistry", "maths", "cs")
from django import forms
from .models import Projects,Profile


class ProjectsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['editor', 'pub_date']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

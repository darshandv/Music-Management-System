from django.contrib.auth import get_user_model
from django import forms

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First Name', required = True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

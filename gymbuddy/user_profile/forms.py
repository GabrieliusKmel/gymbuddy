from django import forms
from django.contrib.auth import get_user_model
from . import models
from django.contrib import messages 

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['height', 'weight', 'gender']

    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        gender = cleaned_data.get('gender')

        if not height or not weight or not gender:
            self._errors['__all__'] = self.error_class([])
            del cleaned_data['height']
            del cleaned_data['weight']
            del cleaned_data['gender']

        return cleaned_data
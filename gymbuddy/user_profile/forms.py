from django import forms
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['height', 'weight', 'age', 'gender', 'activity_level', 'weight_goal']
        widgets = {
            'gender': forms.Select,
            'activity_level': forms.Select,
            'weight_goal': forms.Select,
        }
        labels = {
            'height': 'Height (cm):',
            'weight': 'Weight (kg):',
        }

    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        age = cleaned_data.get('activity_level')
        age = cleaned_data.get('weight_goal')

        if not height or not weight or not gender or not age:
            self._errors['__all__'] = self.error_class([])
            del cleaned_data['height']
            del cleaned_data['weight']
            del cleaned_data['gender']
            del cleaned_data['age']
            del cleaned_data['activity_level']
            del cleaned_data['weight_goal']
        return cleaned_data

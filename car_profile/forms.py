from django import forms

from car_profile.models import CarProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CarProfile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'age': "Age requirement: 21 years and above.",
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CarProfile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = CarProfile
        fields = ()

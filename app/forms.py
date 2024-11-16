from django import forms

from . models import Register

class UserForms(forms.Form):
    username = forms.CharField(max_length=50)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("password do not match")
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email']


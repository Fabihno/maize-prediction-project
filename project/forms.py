from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


gender_choices = [
    ('Mr', 'Male'),
    ('Mrs', 'Female'),
    ('Other', 'Other')
]
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Enter email')
    gender = forms.CharField(max_length=10,  
        widget=forms.Select(choices=gender_choices),
        )
    dob = forms.DateField(label='Enter date of birth', help_text="Please use the following format: <em>MM-DD-YYYY</em>.")

    #radio = forms.CheckboxInput('male', 'female')


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        return dob

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        return gender

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            #self.cleaned_data['gender'],
            self.cleaned_data['password1']
            
        )
        user = User.objects.create_user(
            self.cleaned_data['dob'],
        )
        return user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Електрона адреса'
    }))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'пароль'
    }))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'повторіть пароль'
    }))

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "ім'я"
    }))

    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "призвіще"
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class LoginForm(AuthenticationForm):
    """
    redefined class
    Father AuthenticationForm
    I change attribute widget
    """

    def __init__(self, *args, **kwargs):
        """
        redefined widget i change attribute widget
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Електрона адреса'
        })
        self.fields['username'].label = ''

        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Пароль'
        })
        self.fields['password'].label = ''

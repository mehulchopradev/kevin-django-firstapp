from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }), error_messages={
        'required': 'Username is required'
    })
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }), error_messages={
        'required': 'Password is required'
    })

class RegisterForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }), error_messages={
        'required': 'Username is required'
    })
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }), error_messages={
        'required': 'Password is required'
    })
    country = forms.ChoiceField(choices=(('IN', 'India'),('US', 'USA')))
    gender = forms.ChoiceField(widget=forms.RadioSelect(),\
        choices=(('m', 'Male'), ('f', 'Female')), error_messages={
            'required': 'Gender is required'
        })

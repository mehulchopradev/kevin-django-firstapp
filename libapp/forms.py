from django import forms
from libapp.models import Student

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

''' class RegisterForm(forms.Form):
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
        }) '''

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'password', 'country', 'gender', 'profilepicpath')

        labels = {
            'username': '',
            'password': ''
        }

        error_messages = {
            'username': {
                'required': 'Username is required'
            },
            'password': {
                'required': 'Password is required'
            }
        }

        widgets = {
            'username': forms.TextInput(attrs={
                            'placeholder': 'Enter username'
                        }),
            'password': forms.PasswordInput(attrs={
                            'placeholder': 'Enter password'
                        })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # database code/service call to get say e.g. countries
        countries = (('IN', 'India'),('US', 'USA'))

        self.fields['country'] = forms.ChoiceField(choices=countries)
        self.fields['gender'] = forms.ChoiceField(widget=forms.RadioSelect(),\
            choices=(('m', 'Male'), ('f', 'Female')), error_messages={
                'required': 'Gender is required'
            })
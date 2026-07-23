from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_attr(self.fields['username'], 'css', 'a-css-class')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Your first name. ex: John')
        add_placeholder(self.fields['last_name'], 'Your last name. ex: Doe')
    
    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput({
            'placeholder' : 'Your password.'
        })
        )
    password2 = forms.CharField(
        required=True,
        widget= forms.PasswordInput({
            'placeholder' : 'Confirm your password here.'
        }),

        error_messages={
            'required' : 'Password must not be empty'
        },

        help_text = 'Password must have atleast one uppercase letter, one lowercase letter and on number. The length should be atleast 8 characters'
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name' : 'First name',
            'username' : 'Username',
            'last_name' : 'Last name',
            'email' : 'E-mail',
            'password' : 'Password'
        }

        help_texts = {
            'email' : 'Please use an existing e-mail',
        }

        error_messages = {
            'username' : {
                'required' : 'This field must not be empty',
            },
        }

        widgets = {
            'first_name' : forms.TextInput({
                'placeholder' : 'Type your first name here',
            }),
            'username' : forms.TextInput({
                'placeholder' : 'Type your username here.',
            }),

            'email' : forms.EmailInput({
                'placeholder' : 'Write your e-mail here.'
            }),

            'password' : forms.PasswordInput({
                'placeholder' : 'Type your password here',
            })
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data:
            raise ValidationError(
                'Não digite "%(value)s" neste campo',
                code='invalid',
                params={'value' : 'atenção'}
            )

        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password2':'password and password2 must be equal',
            },
            code= 'invalid'
            )
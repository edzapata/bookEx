from django import forms
from django.forms import ModelForm
from .models import Book, User
from .filters import BookFilter


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'web': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'picture': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'id': 'image-upload',
                'required': True
            }),
        }

class UserInfoForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            # 'email',
            'street',
            'city',
            'state',
            'zipcode',

        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            # 'email': forms.TextInput(
            #     attrs={
            #         'class': 'form-control'
            #     }
            # ),
            'street': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'zipcode': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),


        }

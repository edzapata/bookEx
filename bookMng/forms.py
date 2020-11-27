from django import forms
from django.forms import ModelForm
from .models import Book
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

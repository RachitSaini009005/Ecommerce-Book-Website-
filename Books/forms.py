from django import forms
from .models import Books_author_book_registration

class BookForm(forms.ModelForm):
    class Meta:
        model = Books_author_book_registration
        fields = '__all__'

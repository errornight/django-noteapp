from django import forms
from .models import Category, Note


def get_tags():
    # this function returns all tag objects
    return [(category.id, category.title.upper()) for category in Category.objects.all()]

class AddNote(forms.Form):
    title = forms.CharField(max_length=120, label='Note title:')
    short_desc = forms.CharField(max_length=100, label='Short description:',
                                 widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter a short description for your note...'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))
    category = forms.ChoiceField(label='Tag', choices=get_tags)
    public = forms.BooleanField(required=False, label='Is your note public?')


class EditNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'short_desc', 'body', 'category', 'public']



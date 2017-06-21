from django import forms


class RequestForm(forms.Form):
    q = forms.CharField(
        label='Search for:',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'What we will search in books?'}
        )
    )
    email = forms.EmailField(
        label='Email for results:',
        widget=forms.TextInput(
            attrs={'placeholder': 'Your email for search results'}
        )
    )

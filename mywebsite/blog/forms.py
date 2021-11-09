from django import forms

class postForm(forms.Form):
    Name            = forms.CharField(
        label       = 'Name',
        max_length  = 30,
        widget      = forms.TextInput(
            attrs   = {
                'class' : 'form-control',
            }
        )
    )
    Email           = forms.EmailField(
        max_length  = 50,
        label       = 'Email address',
        widget      = forms.EmailInput(
            attrs   = {
            'class' : 'form-control',
            }
        )
    )
    Mail            = forms.CharField(
        widget      = forms.Textarea(
            attrs   = {
                'class' : 'form-control',
                'rows' : "3"
            }
        )
    )
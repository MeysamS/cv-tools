from django import forms

class Contact_us_send_Form(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
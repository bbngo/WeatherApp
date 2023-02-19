from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label='Please enter a valid U.S. address', max_length=100, widget= forms.TextInput(attrs={'placeholder': 'Please enter a valid U.S. address'}))
from django import forms

class PhoneNumberForm(forms.Form):
	phone_number = forms.CharField(label='Phone number')

class VerifyPINForm(forms.Form):
	phone_number = forms.CharField(label='Phone number')
	pin = forms.CharField(label='PIN')

from django import forms
from .models import Event, Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class EventForm(forms.ModelForm):
    title = forms.TextInput()
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Enter Event...'
            }))
    event_date = forms.DateField()
    event_time = forms.TimeInput()
    street = forms.TextInput()
    city = forms.TextInput()
    state = forms.TextInput()
    zip_code = forms.IntegerField()

    class Meta:
        model = Event
        fields = ['title', 'body', 'event_date', 'event_time', 'street', 'city', 'state', 'zip_code']

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': ('8883459876')}),
        label=('Phone Number')
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Enter Message'
            }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']


    

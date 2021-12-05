from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Event(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True, default='')
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    website = models.URLField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    email = models.EmailField(max_length=150, default='')
    phone_number = PhoneNumberField(default='')
    message = models.TextField()

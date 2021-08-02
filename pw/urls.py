from django.urls import path
from .views import (
    EventCreate, 
    EventListView, 
    Index, 
    ContactView, 
    About, 
    EventDetailView, 
    EventEditView, 
    EventDeleteView, 
    Services,
    Resources,
    Process,
    Consult
    )

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
    path('resources/', Resources.as_view(), name='resources'),
    path('process/', Process.as_view(), name='process'),
    path('consult/', Consult.as_view(), name='consult'),
    path('event/', EventListView.as_view(), name='event_list'),
    path('event/create', EventCreate.as_view(), name='event_create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/edit/<int:pk>/', EventEditView.as_view(), name='event_edit'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('contact/', ContactView.as_view(), name='contact'),
] 
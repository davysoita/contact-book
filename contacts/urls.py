from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('contacts/<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('contacts/<int:pk>/delete/', views.delete_contact, name='delete_contact'),
]
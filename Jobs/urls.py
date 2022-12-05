from django.urls import path, include
from .views import *

urlpatterns = [
  path('', homepage, name='home'),
  path('services/', servicesPage, name='services'),
  path('employers/', employerPage, name='employer'),
  path('faqs/', faqsPage, name='faqs'),
  path('jobs/', job_seeker_page, name='job seeker'),
  path('contacts/', contactPage, name='contact'),
  path('error/', errorPage, name='error'),

]

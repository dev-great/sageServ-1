from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServicesView.as_view(), name='service'),
    path('recources/', ResourcesView.as_view(), name='recources'),
    path('finder/', FinderView.as_view(), name='finder'),
    path('contact/', ContactView.as_view(), name='contact'),
]

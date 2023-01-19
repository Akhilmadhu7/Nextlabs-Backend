from django.urls import path
from . views import *

urlpatterns = [
    path('hello',Hello.as_view(),name='hello'),
    path('signup',SignupView.as_view(),name='signup'),
    path('add-app',AddApplication.as_view(),name='add-app')

]

from django.urls import path
from . views import *

urlpatterns = [
    path('hello',Hello.as_view(),name='hello'),
    path('signup',SignupView.as_view(),name='signup'),
    path('add-app',AddApplication.as_view(),name='add-app'),
    path('list-apps',ListApplication.as_view(),name='list-apps'),
    path('delete-app/<int:id>',delete_app,name='delete-app'),
    path('user-profile',UserProfile.as_view(),name='user-profile'),
    path('task-complete',TaskComplete.as_view(),name='task-complete'),
    path('app-details/<int:id>',AppDetailsView.as_view(),name='app-detail')

]

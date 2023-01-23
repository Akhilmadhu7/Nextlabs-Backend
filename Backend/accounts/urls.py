from django.urls import path
from . views import *

urlpatterns = [
    #signup url
    path('signup',SignupView.as_view(),name='signup'),
    #add application  url
    path('add-app',AddApplication.as_view(),name='add-app'),
    #list applications side url
    path('list-apps',ListApplication.as_view(),name='list-apps'),
    #delete app on admin side url
    path('delete-app/<int:id>',delete_app,name='delete-app'),
    #userprofile url 
    path('user-profile',UserProfile.as_view(),name='user-profile'),
    #task url user
    path('task-complete',TaskComplete.as_view(),name='task-complete'),
    #app details url 
    path('app-details/<int:id>',AppDetailsView.as_view(),name='app-detail')

]

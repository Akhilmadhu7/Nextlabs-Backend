from django.contrib import admin
from . models import Accounts, ApplicationModel, TaskModel

# # Register your models here.

admin.site.register(Accounts)

admin.site.register(ApplicationModel)

admin.site.register(TaskModel)
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.


class AccountsManager(BaseUserManager):

    def _create_user(self,username,email,password,is_staff,is_active,is_admin,is_superadmin):
        if not username:
            raise ValueError("User must have username")
        if not email:
            raise ValueError("User must have email")
        email = self.normalize_email(email)   
        user = self.model(username=username,email=email,is_staff=is_staff,is_active=is_active,is_admin=is_admin,is_superadmin=is_superadmin)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,password,**extra_fields):
        return self._create_user(username,email,password,
            is_staff=False,is_active=True,is_admin=False,is_superadmin=False,**extra_fields)   

    def create_superuser(self,username,email,password,**extra_fields):
        user = self._create_user(username,email,password,is_staff=True,is_active=True,is_admin=True,
        is_superadmin=True)  
        user.save(using=self.db)
        return user            


class Accounts(AbstractBaseUser):

    username = models.CharField(max_length=120,unique=True)
    email = models.EmailField(max_length=200,unique=True)
    profile_pic = models.ImageField(upload_to='profileImage',null=True,blank=True)
    user_points = models.CharField(max_length=120,default=0)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountsManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class ApplicationModel(models.Model):

    created_user = models.CharField(max_length=120,null=True)
    app_name = models.CharField(max_length=120,unique=True)
    app_link = models.CharField(max_length=200)
    app_image = models.ImageField(upload_to='applicationImage')
    app_category = models.CharField(max_length=120)
    app_subcategory = models.CharField(max_length=120)
    app_points = models.CharField(max_length=120)

    def __str__(self):
        return self.app_name


class TaskModel(models.Model):

    application = models.ForeignKey(ApplicationModel,related_name='application_name',on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts,related_name='user_name',on_delete=models.CASCADE)
    task_image = models.ImageField(upload_to='taskImage',null=True,blank=True)

    def __str__(self):
        return self.application.app_name
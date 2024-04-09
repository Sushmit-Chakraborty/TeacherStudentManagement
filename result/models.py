from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group

# create a new user

class MyAccontManager(BaseUserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Please enter a valid email.")
        if not username:
            raise ValueError("Please enter a valid user.")
        user = self.model(
            email=self.normalize_email(email), 
            username=username,
            )
        user.set_password(password)
        user.save(using=self._db)       
        
        return user
    
    # create a super user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), 
            username=username, 
            password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    contact = models.IntegerField(default=9999)
    category = models.CharField(max_length=20, choices=[('teacher', 'Teacher'), ('student', 'Student')], default='no category')
    groups = models.ManyToManyField(Group, blank=True)

    objects = MyAccontManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def __str__(self):
    #     return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class ResultDb(models.Model):
    email = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    english = models.IntegerField(default=0)  
    bengali = models.IntegerField(default=0)
    mathematics = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    programming = models.IntegerField(default=0)
    environment = models.IntegerField(default=0)


    def calculate_total(self):
        return self.english + self.bengali + self.mathematics + self.science + self.programming + self.environment
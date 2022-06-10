from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,email, password, first_name, lat_name, **extra_fields):
        if not email:
           raise ValueError("Email must be provided")
        if not password:
           raise ValueError("password is not provided")
        user= self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            lat_name= lat_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email, password, first_name, lat_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_suoeruser',False)
        return self._create_user(email, password, first_name, lat_name,**extra_fields)

    def create_superuser(self, email, password, first_name, lat_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, lat_name,**extra_fields)
   

class user(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    lat_name=models.CharField(max_length=255)
    is_staff= models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

    objects= CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name','lat_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

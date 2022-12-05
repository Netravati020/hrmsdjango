


from django.db import models
from django.contrib.auth.models import AbstractUser, User


from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations= True


    def create_user(self,employee_id,password=None,**other_fields):
        # if not employee_id:
        #     raise ValueError('you must provide Employee_id')
        # employee_id= self.normalize_email(employee_id)
        user=self.model(employee_id=employee_id,**other_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user


    def create_superuser(self,employee_id,password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff')is not True:
            raise ValueError('Superuser must be signed to is_staff=true')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be signed to is_superuser=true')
        return self.create_user(employee_id,password,**other_fields)

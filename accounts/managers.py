from django.db import models
from django.contrib.auth.models import BaseUserManager






class MyUserManager(BaseUserManager):
    def create_user(self, email,full_name, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            full_name=full_name,
            email=self.normalize_email(email),
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,full_name, phone_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,full_name, phone_number, password)
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password, user_name,
                    father_name, mother_name, nationality, photo,
                    mobile, ssc_marks, inter_marks):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            password=password,
            user_name=user_name,
            father_name=father_name,
            mother_name=mother_name,
            nationality=nationality, photo=photo,
            mobile=mobile, ssc_marks=ssc_marks,
            inter_marks=inter_marks
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """
    create user
    """
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    user_name = models.CharField(max_length=255, verbose_name="User Name",
                                 blank=True)
    father_name = models.CharField(max_length=255, verbose_name="Father Name",
                                   blank=True)
    mother_name = models.CharField(max_length=255, verbose_name="Mother Name",
                                   blank=True)
    nationality = models.CharField(max_length=255, verbose_name="Nationality",
                                   blank=True)
    mobile = models.IntegerField(blank=True, verbose_name="Mobile Number")
    photo = models.ImageField(upload_to='user/images', blank=True,
                              verbose_name="Image")
    ssc_marks = models.IntegerField(blank=True, verbose_name="SSC Marks")
    inter_marks = models.IntegerField(blank=True, verbose_name="Inter Marks")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete = models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete = models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete = models.CASCADE)
    size = models.ForeignKey(Size, on_delete = models.CASCADE)
    Chicken = models.BooleanField(default=False)
    Pepperoni = models.BooleanField(default=False)
    Mushroom = models.BooleanField(default=False)
    Olives = models.BooleanField(default=False)
    Ham = models.BooleanField(default=False)
    Pineapple = models.BooleanField(default=False)
    Peppers = models.BooleanField(default=False)
    Onion = models.BooleanField(default=False)
    Sweetcorn = models.BooleanField(default=False)
    Pesto = models.BooleanField(default=False)
    Anchovies = models.BooleanField(default=False)
    Jalapeno = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    card_number = models.CharField(max_length=16)
    card_expiry = models.DateTimeField(null=True)
    card_cvv = models.CharField(max_length=3)
    order_time = models.DateTimeField(auto_now_add=True)

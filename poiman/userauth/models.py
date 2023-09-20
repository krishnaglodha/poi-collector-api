from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
categorytypes = [
    ('normal','normal'),
    ('manager','manager')
    ]
class AppUser(AbstractUser):
    """
    This class is used to create a custom user model.
    This allows users to be classified as either a normal user or a manager.
    """
    category = models.CharField(choices=categorytypes,default='normal', max_length=50)
    
    # Save feature to convert password to hash format.
    def save(self,*args, **kwargs):
        user = super(AppUser, self)
        user.set_password(self.password)
        user.save()
        return user
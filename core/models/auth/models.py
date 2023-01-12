from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

from PIL import Image
from django.conf import settings
import os

def user_directory_path_profile(instance, filename):

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    # if os.path.exists(full_path):
    #     os.remove(full_path)

    return profile_pic_name


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=50, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to=user_directory_path_profile, blank=True, null=True, verbose_name='Picture')


    #! this is the function that will resize the image need to fix
    # def save(self, *args, **kwargs):
    #     SIZE = 250, 250
    #     if self.picture:
    #         pic = Image.open(self.picture.path)
            
    #         pic.thumbnail(SIZE, Image.LANCZOS)
    #         if pic.mode != 'RGB':
    #             pic = pic.convert('RGB')
    #         pic.save(self.picture.path)

    def __str__(self):
        return self.user.username    


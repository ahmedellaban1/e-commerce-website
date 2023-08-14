from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from rules.numbers_validators import PHONE_NUMBER_PATTERN
from rules.file_uploader import image_uploader


# Create your models here.


class Profile(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField(upload_to=image_uploader('Profile'), null=True, blank=False)
    phone = models.CharField(
        max_length=11, blank=False, null=False,
        validators=[PHONE_NUMBER_PATTERN]
    )
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    code = models.CharField(max_length=6, blank=True, null=True, default='')

    def save(self, *args, **kwargs):
        self.slug = ''
        text = f'{self.user} {self.user.id}'
        self.slug = slugify(text)
        super(Profile, self).save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return f"id={self.id}, user = {self.user.username}"


class Address(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=50,null=False, blank=False)

    def __str__(self):
        return f"id={self.id}, address={self.address}, user = {self.user.username}, company = {self.company}"

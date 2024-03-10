from django.db import models
from django.conf import settings
import random
import string


def generate_tinyurl():
    length = 10
    characters = string.ascii_letters + string.digits
    unique = False
    while not unique:
        tinyurl = ''.join(random.choice(characters) for _ in range(length))
        unique = not URL.objects.filter(tinyurl=tinyurl).exists()
    return tinyurl


class URL(models.Model):
    tinyurl = models.CharField(max_length=10, unique=True, default=generate_tinyurl)
    originalUrl = models.URLField(max_length=1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    createDatetime = models.DateTimeField(auto_now_add=True)
    numberOfRedirects = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.tinyurl:
            self.tinyurl = generate_tinyurl()
        super(URL, self).save(*args, **kwargs)


class Redirect(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    datetime = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

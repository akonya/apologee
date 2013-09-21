from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #class to hold user profile data
    user = models.ForeignKey(User, unique = True)
    name = models.CharField(max_length = 200)


class Apology(model.Model):
    #class to hold apologies
    sentFrom = models.ForeignKey(UserProfile)
    sentTo = models.ForeignKey(UserProfile)
    text = models.CharField(max_length = 500)
    mutual = models.BooleanFeild(default = False)

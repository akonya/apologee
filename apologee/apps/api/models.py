from django.db import models
from django.contrib.auth.models import User
import string
import random

class UserProfile(models.Model):
    #class to hold user profile data
    user = models.ForeignKey(User, unique = True)
    name = models.CharField(max_length = 200)
    token  = models.CharField(max_length = 100, default = 'blank')

    def __unicode__(self):
        return self.name

    def getToken(self):
        chars = string.ascii_uppercase+string.digits+string.ascii_lowercase
        tokenbase = ''.join(random.choice(chars) for x in range(25))
        token = self.name + tokenbase
        self.token = token
        self.save()
        return token


class Apology(models.Model):
    #class to hold apologies
    sentFrom = models.ForeignKey(UserProfile, related_name = "sent_from")
    sentTo = models.ForeignKey(UserProfile, related_name = "sent_to")
    text = models.CharField(max_length = 500, default = 'blank')
    mutual = models.BooleanField(default = False)

    def __unicode__(self):
        return "%s->%s" % (
            self.sentFrom.name,
            self.sentTo.name
        )

    def accept(self):
        #applogy accepted
        self.mutual = True
        self.save()
 

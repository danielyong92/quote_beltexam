from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import *

# MODELS FOR QUOTE APP

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) == 0:
            errors['no_author'] = "You Must Enter Author!"
        elif len(postData['quote']) == 0:
            errors['no_quote'] = "Quote cannot be blank!"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=45)
    quote = models.TextField()
    user = models.ForeignKey(User, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name="liked_message")
    objects = QuoteManager()

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from enum import Enum

class Permission(Enum):
    user = 1
    admin = 2
    
class ForumUser(User):
    permission = models.IntegerField(default = 1)

class Document(models.Model):
    
    content = HTMLField()
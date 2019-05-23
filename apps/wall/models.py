######### FOR THE WALLLLLLL #########
from django.db import models
from ..valid.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_on_m = models.ManyToManyField(User, related_name= "messages_liked")

class Comments(models.Model):
    comment = models.TextField()
    messages = models.ForeignKey(Message, related_name="commentsm") # links one to many on message can have many comments but one comment can not have many messages
    user = models.ForeignKey(User, related_name="commentsu") # links one to many on user can have many comments but one comment can not have many user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_on_c = models.ManyToManyField(User, related_name= "comments_liked")



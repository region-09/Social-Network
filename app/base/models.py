from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField()

class Friend(models.Model):
    # Define the two users who are friends
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_friends')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_friends')
    last_message_date = models.DateTimeField()

class Media(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    reposter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reposter')
    media = models.FileField(upload_to='publications',null=True, blank=True)
    description = models.TextField()
    upload_date = models.DateTimeField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_media = models.ForeignKey(Media, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='comment_media')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

class Shared(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='shared_media')

class ProfileInfo(models.Model):
    degree = models.CharField(max_length=100, null=True, blank=True, default='')
    workplace = models.CharField(max_length=100, null=True, blank=True, default='')
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='profile_images/', null=True, blank=True, default='/profile_images/default.png')


class Requests(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    accepted = models.BooleanField(default=False)

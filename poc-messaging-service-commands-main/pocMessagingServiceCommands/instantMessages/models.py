from django.db import models
import uuid


# Create your models here.
class UserCreatedConversation(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=100)
    name = models.CharField(max_length=100)
    creator_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100, default="userCreatedConversation")
    created_at = models.DateTimeField(auto_now_add=True)


class UserAddedParticipantToConversation(models.Model):
    user_id = models.CharField(max_length=100)
    participant_id = models.CharField(max_length=100)
    conversation_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100, default="userAddedParticipantToConversation")
    created_at = models.DateTimeField(auto_now_add=True)


class UserRemovedParticipantToConversation(models.Model):
    user_id = models.CharField(max_length=100)
    participant_id = models.CharField(max_length=100)
    conversation_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100, default="userRemovedParticipantToConversation")
    created_at = models.DateTimeField(auto_now_add=True)


class UserSentMessageToConversation(models.Model):
    user_id = models.CharField(max_length=100)
    conversation_id = models.CharField(max_length=100)
    message_content = models.TextField()
    event = models.CharField(max_length=100, default="userSentMessageToConversation")
    created_at = models.DateTimeField(auto_now_add=True)


class UserDeletedConversation(models.Model):
    user_id = models.CharField(max_length=100)
    conversation_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100, default="userDeletedConversation")
    created_at = models.DateTimeField(auto_now_add=True)







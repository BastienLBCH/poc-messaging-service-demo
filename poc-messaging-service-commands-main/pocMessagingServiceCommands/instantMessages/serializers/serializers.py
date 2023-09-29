from rest_framework import serializers
from ..models import \
    UserCreatedConversation, \
    UserAddedParticipantToConversation, \
    UserRemovedParticipantToConversation, \
    UserSentMessageToConversation, \
    UserDeletedConversation


# Serializer for the even generated when a user creates a conversation
class UserCreatedConversationModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    creator_id = serializers.CharField(required=True)

    class Meta:
        model = UserCreatedConversation
        fields = "__all__"


# Serializer for the event generated when a user added a participant to a conversation
class UserAddedParticipantToConversationModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    participant_id = serializers.CharField(required=True)
    conversation_id = serializers.CharField(required=True)

    class Meta:
        model = UserAddedParticipantToConversation
        fields = "__all__"


# Serializer for the event generated when a user removed a participant from a conversation
class UserRemovedParticipantToConversationModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    participant_id = serializers.CharField(required=True)
    conversation_id = serializers.CharField(required=True)

    class Meta:
        model = UserRemovedParticipantToConversation
        fields = "__all__"


# Serializer for the event generated when a user sent a participant to a conversation
class UserSentMessageToConversationModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    conversation_id = serializers.CharField(required=True)
    message_content = serializers.CharField(required=True)

    class Meta:
        model = UserSentMessageToConversation
        fields = "__all__"


# Serializer for the event generated when a user deleted a conversation
class UserDeletedConversationModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    conversation_id = serializers.CharField(required=True)

    class Meta:
        model = UserDeletedConversation
        fields = "__all__"











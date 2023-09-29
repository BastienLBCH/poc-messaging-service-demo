import json

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from .serializers.serializers import \
    UserCreatedConversationModelSerializer, \
    UserAddedParticipantToConversationModelSerializer, \
    UserRemovedParticipantToConversationModelSerializer, \
    UserSentMessageToConversationModelSerializer, \
    UserDeletedConversationModelSerializer

import jwt


@api_view(["GET"])
def test(request):
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def userCreatedConversation(request):
    """
    Register an event signaling the user created a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")

    # data = JSONParser().parse(request)
    data = request.data.copy()
    data["creator_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]

    serializer = UserCreatedConversationModelSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userAddedParticipantToConversation(request, conversation_id):
    """
    Register an event that a user added a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]
    data["conversation_id"] = conversation_id

    serializer = UserAddedParticipantToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userRemovedParticipantToConversation(request, conversation_id, participant_id):
    """
    Register an event that a user removed a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]
    data["conversation_id"] = conversation_id
    data["participant_id"] = participant_id

    serializer = UserRemovedParticipantToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userSentMessageToConversation(request, conversation_id):
    """
    Register an event that a user sent a message to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]
    data["conversation_id"] = conversation_id

    serializer = UserSentMessageToConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def userDeletedConversation(request, conversation_id):
    """
    Register an event that a user added a participant to a conversation
    :param request:
    :return:
    """
    name, token = request.headers["Authorization"].split(" ")
    data = request.data.copy()
    data["user_id"] = jwt.decode(token, options={"verify_signature": False})["sub"]
    data["conversation_id"] = conversation_id

    serializer = UserDeletedConversationModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




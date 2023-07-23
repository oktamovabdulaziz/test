from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView,\
    UpdateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, DestroyAPIView
from rest_framework.response import Response


@api_view(['GET'])
def get_person(request, pk):
    gender = Gender.objects.get(id=pk)
    person = Person.objects.filter(gender=gender)
    data = PersonSerializer(person, many=True).data
    return Response({"data": data})



@api_view(['GET'])
def get_friend(request, pk):
    person = Person.objects.get(id=pk)
    friend = Friendship.objects.filter(friend1=person)
    frien = Friendship.objects.filter(friend2=person)
    friends = []
    for i in friend:
        friends.append(i.friend1)
    return Response({f"{i.friend1}"})


@api_view(['GET'])
def get_gender(request, pk):
    location = Location.objects.get(id=pk)
    person = Person.objects.filter(location=location)
    men = 0
    women = 0
    for i in person:
        if Person.objects.filter(gender=i.gender):
            if i.gender.name == Gender.name:
                men += 1
            if i.gender.name == 'Women':
                women += 1
    return Response({"men": men, "women": women})


@api_view(['GET'])
def get_gender_type(request, pk):
    person = Person.objects.get(id=pk)
    friend1 = Friendship.objects.filter(friend1=person)
    friend2 = Friendship.objects.filter(friend2=person)
    gender_id = []
    for i in friend1:
        if not i.friend1.gender.id in gender_id:
            gender_id.append(i.friend1.gender.id)
    for i in friend2:
        if not friend2.gender.id in gender_id:
            gender_id.append(i.friend2.gender.id)
    return Response({"count": len(gender_id)})

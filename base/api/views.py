from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from base.models import Room

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api'},
        {'GET':'/api/rooms'},
        {'GET':'/api/rooms/:id'},
        ]
    
    return Response(routes)

@api_view(['GET'])
def getRooms(request,pk=None):
    
    rooms=Room.objects.get(id=pk) if pk else Room.objects.all()
    serializer=serializers.RoomSerializer(rooms,many=False if pk else True)
    return Response(serializer.data)
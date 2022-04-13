from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from area.models import DhakaSubArea
from area.serializers import DhakaSubAreaSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def dhakaArea(request):
    if request.method == 'GET':
        dhaka = DhakaSubArea.objects.all()
        serialzer = DhakaSubAreaSerializer(dhaka, many=True)
        return Response(serialzer.data)

    if request.method == 'POST':
        serialzer = DhakaSubAreaSerializer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dhakaArea_details(request,name):
    try:
        dhaka = DhakaSubArea.objects.get(name=name.capitalize())
    except DhakaSubArea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DhakaSubAreaSerializer(dhaka)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DhakaSubAreaSerializer(dhaka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        dhaka.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from area.models import DhakaSubArea
from area.serializers import DhakaSubAreaSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def DhakaArea(request):
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


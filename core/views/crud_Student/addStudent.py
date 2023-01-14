
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers.serializerStudent import StudentSerializer

@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
    except:
        return Response({'error': 'error'})
    

    return Response(serializer.data)
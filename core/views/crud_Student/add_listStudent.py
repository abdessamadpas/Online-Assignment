from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers.serializerStudent import StudentSerializer


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Student

from rest_framework import mixins
from rest_framework import generics


# @api_view(['POST'])
# def addStudent(request):
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)       
#         if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class add_listStudent(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset  = Student.objects.all()
    serializer_class  = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers.serializerStudent import StudentSerializer


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Student

from rest_framework import mixins
from rest_framework import generics

class put_delete_Student(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
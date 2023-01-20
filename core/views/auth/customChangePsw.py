from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from core.serializers.serializer import ChangePasswordSerializer


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
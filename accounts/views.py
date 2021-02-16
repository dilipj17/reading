from django.contrib.auth import models
from rest_framework import generics,permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Posts

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],password = validated_data['password'],first_name=validated_data['first_name'],last_name=validated_data['last_name'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DataViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('userid','id','title','body')

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user,context=self.get_serializer_context()).data,"message": "User Created Successfully.  Now perform Login to get your token",})

class DataView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DataViewSerializer
    queryset = Posts.objects.all()
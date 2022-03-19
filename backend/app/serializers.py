from rest_framework import serializers
from .models import Document
from .models import Analyse
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# serializer pre súbor
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file','user_id','analyse_id']

# serializer pre analýzu
class AnalyseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyse
        fields = ['id','user_id','date']

# serializer pre používateľa
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

# serializer pre registráciu
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'first_name', 'last_name')

    # validácia polí
    def validate(self, attrs):
        if len(attrs['username']) < 2:
            raise serializers.ValidationError({"username": "Username must contain at least 2 characters."})
        if len(attrs['username']) > 30:
            raise serializers.ValidationError({"username": "Username cannot contain more than 30 characters."})        
        if len(attrs['first_name']) > 64:
            raise serializers.ValidationError({"first_name": "First name cannot contain more than 64 characters."})  
        if len(attrs['last_name']) > 64:
            raise serializers.ValidationError({"last_name": "Last name cannot contain more than 64 characters."})  
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if len(attrs['password']) > 255:
            raise serializers.ValidationError({"password": "Password cannot contain more than 255 characters."})    
        return attrs

    # vytovrenie User objektu
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework import serializers
from .models import test_data as Test, User_acc


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_acc
        fields = ['id', 'username', 'password', 'role']

    def create(self, validated_data):
        user = User_acc.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'title', 'name']

    def create(self, validated_data):
        return Test.objects.create(**validated_data)

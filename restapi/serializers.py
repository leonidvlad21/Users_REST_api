from rest_framework import serializers
from .models import Userset

# debug new class
class User_Serializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    class Meta:
        model = Userset
        # fields = ('id', 'name', 'email')
        fields = "__all__"

class UserPatchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)
    class Meta:
        model = Userset
        fields = ('id', 'name', 'email', 'register_date')

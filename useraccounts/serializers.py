from rest_framework import serializers
from . models import register

class register_ser(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['first_name','username','email','password']

class login_ser(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['email','password']




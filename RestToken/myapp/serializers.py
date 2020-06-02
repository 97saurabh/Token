from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSeri(serializers.ModelSerializer):

    password2 =  serializers.CharField(style={'input_type':'password'},write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'Password': "Not Matching"})
        return data
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password','password2']

        extrakwargs = {
            'password' : {'write_only':True}
        }
    def save(self):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

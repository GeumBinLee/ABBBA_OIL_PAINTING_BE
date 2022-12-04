from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
import re
from painters.serializers import ImageCreateSerializer
from painters.models import Painting


class UserSerializer(serializers.ModelSerializer):
    # 패스워드 확인은 serialization하지 않는다.
    password_check= serializers.CharField(error_messages={"write_only":True,'required':'비밀번호 확인까지 입력해 주세요.', 'blank':'비밀번호 확인까지 입력해 주세요.'}) 

    class Meta:
        model = User
        fields = ("email", "nickname", "password", "password_check")
        extra_kwargs = {
            "email" :{"error_messages" : {
                "required" : "이메일을 입력해 주세요.",
                "blank" : "이메일을 입력해 주세요."}},
            "nickname" : {"error_messages":{
                "required":"닉네임을 입력해 주세요.",
                "blank":"닉네임을 입력해 주세요."}},
            "password" : {"write_only":True, # password도 직렬화하지 않는다.
                          "error_messages":{
                "required":"비밀번호를 입력해 주세요.",
                "blank":"비밀번호를 입력해 주세요."}},
        }

    def validate(self, validated_data):
        email = validated_data.get("email")
        email_reg = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        password_reg = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$"
        password = validated_data.get("password")
        password_check = validated_data.get("password_check")

        # 이메일 유효성 체크
        if not re.search(email_reg, str(email)):
            raise serializers.ValidationError(detail={"email":"이메일 형식에 맞춰서 작성해 주세요."})

        # 비밀번호 유효성 체크
        if not re.search(password_reg, str(password)):
            raise serializers.ValidationError(detail={"password":"최소 한 개의 영문자와 숫자를 포함해 5글자 이상으로 만들어 주세요."})
        elif password != password_check:
            raise serializers.ValidationError(detail={"password":"동일한 비밀번호를 입력해 주세요."})

        return validated_data


    def create(self, validated_data):
        email = validated_data["email"]
        nickname = validated_data["nickname"]
        password = validated_data["password"]
        user = User(
            email = email,
            nickname=nickname,
            password = password
            )
        user.set_password(password)
        user.save()
        return user
    
    def update(self, validated_data):
        email = validated_data["email"]
        nickname = validated_data["nickname"]
        password = validated_data["password"]
        user = User(
            email=email,
            nickname=nickname,
            password = password
            )
        user.set_password(password)
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod 
    def get_token(cls, user):
        token = super().get_token(user)
        token['nickname'] = user.nickname
        
        return token
    
    
class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nickname", "password")
        extra_kwargs = {"password":{"write_only":True, "error_messages":{"blank":"모든 칸을 채워주세요.", "required":"모든 칸을 채워주세요."}}}
    
    def validate(self, validated_data):
        new_password = validated_data.get("password")
        password_reg = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$"
       
        if not re.search(password_reg, str(new_password)):
            raise serializers.ValidationError(detail={"password":"최소 한 개의 영문자와 숫자를 포함해 5글자 이상으로 만들어 주세요."})
        
        return validated_data
    
    def update(self, edit ,validated_data):
        edit.nickname = validated_data["nickname"]
        edit.password = validated_data["password"]
        edit.set_password(edit.password)
        edit.save()
        return edit

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField() 
    
    def get_user(self, obj):
        return obj.user.nickname
    
    class Meta:
        model = Painting
        fields = "__all__"
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# AUTH_USER_MODEL
User = get_user_model()

# 회원 가입 serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["username", "password", "nickname"]
        extra_kwargs = {
            "password": {"write_only": True} # 응답에 password가 나오지 않도록 (작성만 허용)
        }

    # 오류 처리
    def validate(self, data):
        if User.objects.filter(username=data["username"]).exists():
            raise ValidationError(
                {
                    "error": {
                        "code": "USER_ALREADY_EXISTS",
                        "message": "이미 가입된 사용자입니다."
                    }
                }
            )
        return data
    
    # AbstractUser 모델을 썼기 때문에 password를 암호화하여 내부에 저장
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            password = validated_data["password"],
            nickname = validated_data["nickname"],
        )
        return user
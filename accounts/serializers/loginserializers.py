from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        # username 확인
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed(
                {
                    "error": {
                        "code": "INVALID_CREDENTIALS",
                        "message": "아이디 또는 비밀번호가 올바르지 않습니다."
                    }
                }
            )

        # 비밀번호 확인
        if not user.check_password(password):
            raise AuthenticationFailed(
                {
                    "error": {
                        "code": "INVALID_CREDENTIALS",
                        "message": "아이디 또는 비밀번호가 올바르지 않습니다."
                    }
                }
            )
        return data
    
    def save(self, **kwargs):
        # 실제 사용자 객체 반환
        return User.objects.get(username=self.validated_data["username"])
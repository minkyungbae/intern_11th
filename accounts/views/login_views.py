from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import (
    TokenError,
    InvalidToken,
    ExpiredTokenError
    )
from accounts.serializers.loginserializers import LoginSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    @extend_schema(
        tags=["Login"],
        description="로그인을 위한 API",
        request=LoginSerializer,
        examples=[
            OpenApiExample(
                name="Login Example",
                value={
                    "username": "JIN HO",
                    "password": "12341234"
                },
                request_only=True,)])
    
    # 로그인
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)

            return Response({
                    "token": str(refresh)
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 토큰 에러
    def handle_token_error(self, error_type):
        # 토큰 만료
        if error_type == "TOKEN_EXPIRED":
            return Response({
                    "error": {
                        "code": "TOKEN_EXPIRED",
                        "message": "토큰이 만료되었습니다."
                    }}, status=status.HTTP_400_BAD_REQUEST)
        # 토큰을 못 찾은 경우
        elif error_type == "TOKEN_NOT_FOUND":
            return Response({
                    "error": {
                        "code": "TOKEN_NOT_FOUND",
                        "message": "토큰이 없습니다."
                    }}, status=status.HTTP_400_BAD_REQUEST)
        # 유효하지 않는 토큰일 경우
        elif error_type == "INVALID_TOKEN":
            return Response({
                "error": {
                    "code": "INVALID_TOKEN",
                    "message": "토큰이 유효하지 않습니다."
                }}, status=status.HTTP_400_BAD_REQUEST)
        
    # 인증된 토큰일 경우와 예외 처리
    def authenticate_token(self, token):
        try:
            RefreshToken(token)
        except ExpiredTokenError:
            return self.handle_token_error("TOKEN_EXPIRED")
        except InvalidToken:
            return self.handle_token_error("INVALID_TOKEN")
        except TokenError:
            return self.handle_token_error("TOKEN_NOT_FOUND")
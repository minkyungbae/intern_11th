from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers.signupserializers import SignupSerializer
#JWT 토큰
from rest_framework_simplejwt.tokens import RefreshToken
# swagger
from drf_spectacular.utils import extend_schema, OpenApiExample


class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer

    @extend_schema(
        tags=["Signup"],
        description="회원 가입을 위한 API",
        request=SignupSerializer,
        examples=[
            OpenApiExample(
                name="Signup Example",
                value={
                    "username": "JIN HO",
                    "password": "12341234",
                    "nickname": "Mentos"
                },
                request_only=True,)])
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)

            return Response({
                "username": user.username,
                "nickname": user.nickname,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
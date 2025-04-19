import pytest
from rest_framework.test import APIClient
from django.urls import reverse

# 공통 API 클라이언트 설정
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user

# DB 접근을 허용하는 테스트 클래스
@pytest.mark.django_db
class TestLogin:

    # [성공 케이스] 올바른 username과 password를 입력하면 refresh 토큰(token)을 받는다.
    def test_login_success(self, api_client, create_user):
        user = create_user(username="testuser", password="testpass123", nickname="Tester")

        payload = {
            "username": "testuser",
            "password": "testpass123"
        }

        response = api_client.post(reverse("accounts:login"), data=payload, format="json")

        assert response.status_code == 200
        assert "token" in response.data

    # [실패 케이스] 존재하지 않는 사용자로 로그인 시도 시 401 Unauthorized, error message 반환
    def test_login_user_not_found(self, api_client):
        payload = {
            "username": "ghostuser",
            "password": "any_password"
        }

        response = api_client.post(reverse("accounts:login"), data=payload, format="json")

        assert response.status_code == 401
        assert "error" in response.data # error 반환
        assert "message" in response.data["error"] # error라는 딕셔너리 안에서 message 확인

    # [실패 케이스] 비밀번호가 틀린 경우 401 Unauthorized 반환
    def test_login_wrong_password(self, api_client, create_user):
        create_user(username="realuser", password="correctpass")

        payload = {
            "username": "realuser",
            "password": "wrongpass"
        }

        response = api_client.post(reverse("accounts:login"), data=payload, format="json")

        assert response.status_code == 401
        assert "error" in response.data # error 반환
        assert "message" in response.data["error"] # error라는 딕셔너리 안에서 message 확인

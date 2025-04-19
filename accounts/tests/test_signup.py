import pytest
from rest_framework.test import APIClient
from django.urls import reverse

# 공통 API 클라이언트 설정
@pytest.fixture
def api_client():
    return APIClient()

# DB 접근을 허용하는 테스트 클래스
@pytest.mark.django_db
class TestSignup:

    # [성공 케이스] 정상적으로 회원가입 요청을 보낼 경우 201 Created 와 토큰 + 사용자 정보가 응답됨
    def test_signup_success(self, api_client):
        payload = {
            "username": "testuser",
            "password": "strongpassword123",
            "nickname": "Tester"
        }

        response = api_client.post(reverse("accounts:signup"), data=payload, format="json")

        assert response.status_code == 201
        assert "access" in response.data
        assert "refresh" in response.data
        assert response.data["username"] == "testuser"
        assert response.data["nickname"] == "Tester"

    # [실패 케이스] 필수 필드 누락 (password, nickname) 시 400 Bad Request 와 에러 메시지 응답
    def test_signup_missing_fields(self, api_client):
        payload = {
            "username": "testuser"
        }

        response = api_client.post(reverse("accounts:signup"), data=payload, format="json")

        assert response.status_code == 400
        assert "password" in response.data
        assert "nickname" in response.data

    # [실패 케이스] 중복된 username으로 회원가입 시도 시 400 Bad Request 와 에러 메시지 응답
    def test_signup_duplicate_username(self, api_client, django_user_model):
        django_user_model.objects.create_user(username="existinguser", password="1234")

        payload = {
            "username": "existinguser",
            "password": "newpass123",
            "nickname": "Someone"
        }

        response = api_client.post(reverse("accounts:signup"), data=payload, format="json")

        assert response.status_code == 400
        assert "username" in response.data

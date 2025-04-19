# 🔌 *intern_11th 백엔드 개발자(Python) 과제*
[🙋🏻‍♀️ 백엔드 개발자 과제(Python)](https://teamsparta.notion.site/Python-1ad2dc3ef51481c89e92d6bf1020d3e6)

---

## *Swagger Main page*
![swagger-main-page](image/swagger/swagger-main-page.png)
> **Schema를 확인할 수 있고 Signup API와 Login API를 테스트할 수 있습니다.**

---

## *Swagger Signup page*
![swagger-signup-page](image/swagger/signup/swagger-signup-page.png)
> **Examples를 기입하여, 입력값의 예시를 확인할 수 있습니다.**
> 요구된 입력값 : username, password, nickname

### *Signup*
*가입 정보 기입*
![do-signup](image/swagger/signup/swagger-do-signup.png)
> 입력값 : {"username": "test01", "password": "12341234", "nickname": "test"}

*가입 완료*
![do-signup2](image/swagger/signup/swagger-do-signup2.png)
> **username, nickname, access, refresh이 출력됩니다.**
```
Code : 201	
Details:
Response body
{
  "username": "test01",
  "nickname": "test",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDUzNTQyLCJpYXQiOjE3NDUwNTMyNDIsImp0aSI6ImQwNDcyODc4MTIwODRjMmRiOWE4YmEwZDI2MDVlNDhmIiwidXNlcl9pZCI6MX0.yuNTHYhVmH9eckO3SLObNQ-urlHU3mk5cBbFZ9zVDyI",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTEzOTY0MiwiaWF0IjoxNzQ1MDUzMjQyLCJqdGkiOiIxOGY2NTJiMWExZjY0MzZhOGJiNzNhMDk5YzY3NjM1OCIsInVzZXJfaWQiOjF9.VtGEOsrjr0FlPuXUGCicNFyo7yV58jEiQbnVvTUnQgY"
}
```

---

## *Swagger Login page*
![swagger-login-page](image/swagger/login/swagger-login-page.png)
> **Examples를 기입하여, 입력값의 예시를 확인할 수 있습니다.**
> 요구된 입력값 : username, password

### *Login*
![do-login](image/swagger/login/swagger-do-login.png)
> 입력값 : {"username": "test01", "password": "12341234"}

*로그인 완료*
![do-login2](image/swagger/login/swagger-do-login2.png)
> **refresh token이 출력됩니다.**

---

## *Signup 오류 처리*
*Aleady exists*
![Aleady-exists-error](image/swagger/signup/error/swagger-signup-already-exists-error.png)

```
{
  "username": [
    "A user with that username already exists."
  ]
}
```

---
## *Login 오류 처리*
*username or password Invalied error*
![invalied-error](image/swagger/login/error/swagger-login-invalied-error-result.png)

```
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "아이디 또는 비밀번호가 올바르지 않습니다."
  }
}
```
---
## *Auth 오류 처리*
![auth-token-error](image/auth-error/auth-token-error.png)

```python
from rest_framework_simplejwt.exceptions import (
    TokenError,
    InvalidToken,
    ExpiredTokenError
    )

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
```

---
## *폴더 구조*

```
intern_11th
├─ accounts                             <- signup과 login 기능 구현 앱
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers                       <- 사용한 serializers 분리
│  │  ├─ loginserializers.py            <- login serializers.py
│  │  ├─ signupserializers.py           <- signup serializers.py
│  │  └─ __init__.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views                             <- 사용한 views 분리
│  │  ├─ login_views.py                 <- login views.py
│  │  └─ signup_views.py                <- signup views.py
│  └─ __init__.py
├─ image                                <- README.md에 사용할 이미지 관리 폴더
│  ├─ auth-error                        <- 토큰 관련 에러
│  │  └─ auth-token-error.png
│  └─ swagger
│     ├─ login                          <- swagger의 로그인 페이지 소개 및 로그인 과정 사진
│     │  ├─ error                       <- login error 이미지
│     │  │  └─ swagger-login-invalied-error-result.png
│     │  ├─ swagger-do-login.png
│     │  ├─ swagger-do-login2.png
│     │  └─ swagger-login-page.png
│     ├─ signup                         <- swagger의 회원가입 페이지 소개 및 회원가입 과정 소개
│     │  ├─ error                       <- signup error 이미지
│     │  │  └─ swagger-signup-already-exists-error.png
│     │  ├─ swagger-do-signup.png
│     │  ├─ swagger-do-signup2.png
│     │  └─ swagger-signup-page.png
│     └─ swagger-main-page.png
├─ main                                 <- Django 프로젝트 관리 앱
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ pip-install.txt                      <- pip install 명령어 정리
├─ README.md
└─ requirements.txt                     <- 해당 코드를 사용 시, 요구되는 pip list

```
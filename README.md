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

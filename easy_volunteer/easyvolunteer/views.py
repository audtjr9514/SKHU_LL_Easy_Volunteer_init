from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# 맨 첫화면 _ 메인 페이지
def main(request):
    return render(request, 'main.html')

# 소개 페이지
def introduce(request):
    return render(request, 'introduce.html')

# 회원가입에서 기관/일반회원을 고를수 있는 선택 페이지
def select(request):
    return render(request, 'select.html')

# 기관 회원가입 페이지
def organ_signup(request):
    return render(request, 'organ_signup.html')

# 일반 회원가입 페이지
def user_signup(request):
    return render(request, 'user_signup.html')

# 로그인 페이지
def login(request):
    return render(request, 'login.html')

# 일반 회원 마이페이지
def mypage(request):
    return render(request, 'mypage.html')

# 기관용 마이페이지
def organ_mypage(request):
    return render(request, 'organ_mypage.html')

# 기관에서 봉사 등록 페이지
def register(request):
    return render(request, 'register.html')

# 봉사활동을 선택할 수 있는 페이지
def quest(request):
    return render(request, 'quest.html')
    
# 회원이 포인트를 사용할 수 있는 페이지
def point(request):
    return render(request, 'point.html')
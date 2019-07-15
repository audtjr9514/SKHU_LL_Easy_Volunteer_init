from django.shortcuts import render, get_object_or_404, redirect

# 맨 첫화면 _ 메인 페이지
def main(request):
    return render(request, 'main.html')

# 소개 페이지
def introduce(request):
    return render(request, 'introduce.html')

# 회원가입에서 기관/일반회원을 고를수 있는 선택 페이지
def select(request):
    return render(request, 'selct.html')

# 회원가입 페이지
def signup(request):
    return render(request, 'signup.html')

# 로그인 페이지
def login(request):
    return render(request, 'login.html')

# 마이페이지
def mypage(request):
    return render(request, 'mypage.html')

# 봉사활동을 선택할 수 있는 페이지
def quest(request):
    return render(request, 'quest.html')
    
# 회원이 포인트를 사용할 수 있는 페이지
def point(request):
    return render(request, 'point.html')

    
# Create your views here.

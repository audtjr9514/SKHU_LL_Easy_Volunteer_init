# from django import forms
# from .models import User, Organ, Service, Area, Job, Product, Brand


# # 일반회원 회원가입
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = CUser
#         fields = ['email','password','username','codeNum', 'phoneNum', 
#                     'job', 'license', 'area', 'another', 'image']

# # 기관회원 회원가입
# class OrganUserForm(forms.ModelForm):
#     class Meta:
#         model = CUser
#         fields = ['email', 'password', 'username', 'phoneNum', 'area']

# # 기관만의 추가 폼       
# class OrganForm(forms.ModelForm):
#     class Meta:
#         model = Organ
#         fields = ['crew', 'head', 'url' ]

# # 로그인 폼
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = CUser
#         fields = ['email', 'password']

# # 기관에서 봉사활동 등록폼
# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = ['name', 'Essential', 'point', 'level', 'number', 'emergency', 'image']


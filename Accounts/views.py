from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer


def register_view(request):
    """إنشاء حساب جديد"""
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "البريد الإلكتروني مسجل مسبقًا.")
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            Customer.objects.create(full_name=full_name, email=email, phone=phone)
            messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
            return redirect("login")

    return render(request, "Accounts/register.html")


def login_view(request):
    """تسجيل الدخول"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✅")
            return redirect("home")  # يعيدك للصفحة الرئيسية
        else:
            messages.error(request, "خطأ في البريد الإلكتروني أو كلمة المرور.")

    return render(request, "Accounts/login.html")


def logout_view(request):
    """تسجيل الخروج"""
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح 👋")
    return redirect("home")

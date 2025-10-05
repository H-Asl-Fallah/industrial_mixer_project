from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register_view(request):
    """
    این ویو مسئولیت ثبت‌نام کاربر جدید را بر عهده دارد.
    """
    if request.user.is_authenticated:
        return redirect('home') # اگر کاربر لاگین کرده باشد، به صفحه اصلی هدایت می‌شود

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"ثبت‌نام با موفقیت انجام شد. خوش آمدید, {user.username}!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, '../templates/register.html', {'form': form})

def login_view(request):
    """
    این ویو مسئولیت ورود کاربر را بر عهده دارد.
    """
    if request.user.is_authenticated:
        return redirect('home') # اگر کاربر لاگین کرده باشد، به صفحه اصلی هدایت می‌شود

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"شما با موفقیت وارد شدید. سلام, {user.username}!")
                return redirect('home')
            else:
                # این پیام در صورتی نمایش داده می‌شود که نام کاربری یا رمز عبور اشتباه باشد
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
        else:
            # این پیام در صورتی نمایش داده می‌شود که فرم معتبر نباشد
             messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
    
    form = AuthenticationForm()
    return render(request, '../templates/login.html', {'form': form})

def custom_logout_view(request):
    """
    کاربر را از حساب خود خارج کرده، یک پیغام موفقیت نمایش می‌دهد و
    او را به صفحه اصلی سایت هدایت می‌کند.
    """
    logout(request)
    messages.success(request, "شما با موفقیت از حساب کاربری خود خارج شدید.")
    return redirect('home')


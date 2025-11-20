from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from .models import UserProfile

# صفحة تسجيل الدخول
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


# تسجيل الخروج
def logout_user(request):
    logout(request)
    return redirect('login')


# لوحة التحكم – للمدير والمشرف فقط
@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role not in ['admin', 'manager']:
        messages.error(request, "ليس لديك صلاحية الوصول للوحة التحكم")
        return redirect('pos')

    return render(request, 'dashboard.html', {'profile': profile})


# صفحة إدارة المستخدمين – المدير فقط
@login_required
def users_page(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'admin':
        messages.error(request, "هذه الصفحة خاصة بالمدير فقط")
        return redirect('dashboard')

    users = UserProfile.objects.all()

    return render(request, 'users.html', {'users': users})

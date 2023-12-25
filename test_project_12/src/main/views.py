from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from src.main.models import StockPrice
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from src.main.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    volume = request.GET.get('volume')
    if not volume:
        stock_prices = StockPrice.objects.all().values()
    else:
        stock_prices = StockPrice.objects.all().filter(volume=volume).values()
    return render(request, 'main.html', {'stock_prices': stock_prices, 'volume': volume})


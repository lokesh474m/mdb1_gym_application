from django.shortcuts import render

# Create your views here.

def mdb1(request):
    return render(request,'mdb1.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def menu_card(request):
    return render(request,'menu_card.html')

def password(request):
    return render(request,'password.html')

def pushup(request):
    return render(request,'pushup.html')

def running(request):
    return render(request,'running.html')

def push_down(request):
    return render(request,'push_down.html')

def floor_press(request):
    return render(request,'floor_press.html')

def dumbbell_bridge(request):
    return render(request,'dumbbell_bridge.html')

def cardio(request):
    return render(request,'cardio.html')

def calisthenics(request):
    return render(request,'calisthenics.html')

def cable_cross(request):
    return render(request,'cable_cross.html')

def bench_press(request):
    return render(request,'bench_press.html')


from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .models import User, Society, SocietyMember, Notice, Event
# from .forms import LoginForm, RegistrationForm

def home(request):
    return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('home')

# @login_required
# def societies(request):
#     societies = Society.objects.all()
#     return render(request, 'societies.html', {'societies': societies})

# @login_required
# def society_detail(request, society_id):
#     society = Society.objects.get(id=society_id)
#     return render(request, 'society_detail.html', {'society': society})

# @login_required
# def notices(request):
#     notices = Notice.objects.all()
#     return render(request, 'notices.html', {'notices': notices})

# @login_required
# def events(request):
#     events = Event.objects.all()
#     return render(request, 'events.html', {'events': events})
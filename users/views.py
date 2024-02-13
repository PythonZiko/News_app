from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
        
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user:
                    # print("Parol to'gri")
                    login(request, user)
                    return  redirect("create-new")
                
                else:
                    return HttpResponse("<h1>Parol yoki Username topilmadi.</h1>")
                
            else:
                return HttpResponse("<h1>Parol yoki Username topilmadi.</h1>")
    
        return render(request, "users/login.html")
    
    else:
        return  redirect("create-new")



def logout_view(request):
    logout(request)
    return redirect("index")
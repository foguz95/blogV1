from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
#user modelini dahil ediyoruz.
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
#Urls deki yolunu verdiğimiz Fonksiyonları buraya yazıyoruz.

def register(request):
    #Post yada get olduğunu kontrol etmek zorunda değiliz
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        # sisteme kayıt oldu ve login sayesinde otomatik olarak giriş yaptı.
        login(request, newUser)
        messages.info(request,"Başarıyla kayıt oldunuz.")

        return redirect("index")
    #Get durumundada buraya giriyoruz
    context = {
        "form": form
    }
    return render(request, "register.html", context)

    """
    #---------Uzun ve karışık yöntem--------
    if request.method =="POST":
        form=RegisterForm(request.POST)
        #is_valid() i karşılarsa Clean() fonksiyonu çalışacak !
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User(username =username)
            newUser.set_password(password)
            newUser.save()
            #sisteme kayıt oldu ve login sayesinde otomatik olarak giriş yaptı.
            login(request,newUser)

            return redirect("index")

        context = {
            "form": form
        }
        return render(request, "register.html", context)

    else:
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)
    """

    """
    regForm=RegisterForm
    context={
        "form":regForm
    }
    return render(request,"register.html",context)
    """

def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    #formda bir sıkıntı var mı ?
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        kullanici=authenticate(username=username,password=password)

        if kullanici is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,kullanici)
        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("index")

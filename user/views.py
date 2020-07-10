from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from article.models import Article
from article.forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    context = {
            "form" : form
        }
    
    return render(request,"user/register.html",context)
    



def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"user/login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect('user:dashboard')
    return render(request,"user/login.html",context)


def logout(request):
    auth.logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect('index')
    

@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request, 'dashboard.html',context)

@login_required(login_url='user:login')
def update(request,id):
    article=get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        # article.slug = slugify(article.title)
        article.author = request.user
        article.save()

        messages.success(request,"successfully updated")
        return redirect("user:dashboard")
    return render(request,'update.html',{'form':form})

@login_required(login_url='user:login')
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"successfully deleted")
    return redirect('user:dashboard')

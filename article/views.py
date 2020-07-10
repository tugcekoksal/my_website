from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article,Comment
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleForm

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def about(request):
    return render(request,'pages/about.html')
def contact(request):
    return render(request,'pages/contact.html')
def blog(request):
    keyword=request.GET.get('keyword')
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"pages/blog.html",{"articles":articles})

    articles=Article.objects.all()
    return render(request,'pages/blog.html',{"articles":articles})
def post(request,id):
    # articles=Article.objects.filter(id=id)
    article=get_object_or_404(Article,id=id)
   
    
    return render(request,'post.html',{'article':article})

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        # article.slug = slugify(article.title)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("user:dashboard")
    return render(request,"addarticle.html",{"form":form})
        
def comment(request,id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    
    return render(request,'post.html')

        

        

    





    
    
    

    

from django.shortcuts import render, HttpResponse, redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        #bu keyword'ün geçtiği article ları döndürür.
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})

    #Arama işlemi yoksa normal olarak tüm articlelar çekilecek ve ekrana gönderilecek
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    return render(request, "index.html")
    # context={
    # "numbers":[1,2,3,4,5,6]
    # }
    # return HttpResponse("<h3> Anasayfaya hoşgeldiniz </h3>")
    # return render(request,"index.html",{"number":7})
    # return render(request,"index.html",context)


def about(request):
    return render(request, "about.html")

#decorator yukarda kütüphanesi var
@login_required(login_url="user:login")
def dashboard(request):
    # return HttpResponse("Detail: " + str(id)) parametre olarak id ekle

    # login olan kişinin articlelarını bu şekilde dictionary olarak alarak görüyoruz.
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)
#decorator yukarda kütüphanesi var
@login_required(login_url="user:login")
def addArticle(request):
    # artık, formda göstereceğiz.
    # models.pydeki alanlardan yapmamız gerekenleri,
    # forms.py de input oluşturduk.
    # Böylelikle form input oluşturduk.
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        # formdaki bilgilere göre oluşturması için yoksa yazar bilgisini
        # atlıyor ve sadece başlık ve detay kısmını ekliyor. commit=False yaparak
        # formu olduğu gibi alıyoruz.
        article = form.save(commit=False)

        # yazar bilgisini alıyoruz.
        article.author = request.user

        # ve kaydediyoruz.
        article.save()

        messages.success(request, "Makele başarıyla oluşturuldu.")
        #return redirect(index)
        return redirect("article:dashboard")
    return render(request, "addArticle.html", {"form": form})

def detail(request,id):
    #makale başlığını html sayfasında göstermek için bu şekilde alıyoruz...
    #article= Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

#decorator yukarda kütüphanesi var
@login_required(login_url="user:login")
def updateArticle(request,id):
    #Article model içindeki id si id ye eşit olanı alıyor ve güncelliyoruz.
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance = article)

    if form.is_valid():
        article = form.save(commit=False)

        # yazar bilgisini alıyoruz.
        article.author = request.user

        # ve kaydediyoruz.
        article.save()

        messages.success(request, "Makele başarıyla güncellendi.")
        return redirect("article:dashboard")
        #return redirect(index)

    return render(request,"update.html",{"form":form})

#decorator yukarda kütüphanesi var
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)

    article.delete()
    messages.success(request,"Makele başarıyla silindi")
#article uygulaması altındaki dashboarda git
    return redirect("article:dashboard")

#idye göre postu olamamız gerekiyor
def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")

        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article

        newComment.save()
        #dinamik hale getirdik.
        return redirect(reverse("article:detail",kwargs={"id":id}))
        #return redirect("/articles/article/" + str(id))






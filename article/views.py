from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    
    return render(request,"index.html")


def articles(request):
    arama=request.GET.get("arama")

    if arama:
        makaleler=Article.objects.filter(title__contains=arama)
        return render(request,"articles.html",{"makaleler":makaleler})
    makaleler=Article.objects.all()
    return render(request,"articles.html",{"makaleler":makaleler})

def about(request):
    return render(request,"about.html")

@login_required(login_url='user:login')
def kontrolpaneli(request):
    articles = Article.objects.filter(author=request.user)
    #articles=get_object_or_404(Article,author=request.user)
    return render(request,"kontrolpaneli.html",{"articles":articles})

@login_required(login_url='user:login')
def makale_ekle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article=form.save(commit=False)
        
        article.author=request.user
        article.save()
        messages.success(request,"Makale Kaydedildi!")
        return redirect("index")
    return render(request,"makale_ekle.html",{"form":form})


def makale_detay(request,id):

    # article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)
    return render(request,"makale_detay.html",{"article":article})


@login_required(login_url='user:login')
def makale_guncelle(request,id):
    article=get_object_or_404(Article,id=id)

    form =ArticleForm(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        
        article.author=request.user
        article.save()
        messages.success(request,"Makale Güncellendi!")
        return redirect("index")
    return render(request,"makale_guncelle.html",{"form":form})

@login_required(login_url='user:login')
def makale_sil(request,id):
    article=get_object_or_404(Article,id=id)

    article.delete()

    messages.warning(request,"Makale Silindi!")
    return redirect("article:kontrolpaneli")
    

    
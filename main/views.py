from django.shortcuts import render, get_object_or_404, redirect
 
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import DjangoBoard
from django.core.paginator import Paginator
  
def home(request):
    boards = DjangoBoard.objects
    boards_list=DjangoBoard.objects.all()
    paginator = Paginator(boards_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = { 'latest_question_list': "test", 'boards': boards, 'posts':posts }
    
    return render(request, 'main/index.html', context)

def mypage(request):
    return render(request, 'main/mypage.html')

def makeup(request):
    return render(request, 'main/makeup.html')

def beautynail(request):
    return render(request, 'main/beautynail.html')
    
def login(request):
    return render(request, 'main/login.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    boards = DjangoBoard.objects
    boards_list=DjangoBoard.objects.all()
    paginator = Paginator(boards_list,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'main/services.html', {'boards': boards, 'posts':posts})
        
def join(request):
    return render(request, 'main/join.html')

def new(request):
    return render(request, 'main/new.html')

def create(request):
    main = DjangoBoard()
    main.title = request.GET['title']
    main.body = request.GET['body']
    main.price = request.GET['price']
    main.pub_date = timezone.datetime.now()
    main.image = request.GET['image']
    main.save()
    return redirect (services)
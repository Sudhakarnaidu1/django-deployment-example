from django.shortcuts import render

# Create your views here.


def home(request):
    contexxt={'selfinto':'HELLO HOW DO U DO',
              'multi':24,
              'favno':10,
              'div':100}
    return render(request,'temp/home.html',context=contexxt)


def relative(request):
    return render(request,'temp/relative.html')


def other(request):
    return render(request,'temp/other.html')

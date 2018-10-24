from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

randomvar=get_random_string(length=14)
print(randomvar)
# Create your views here.
# djangohw03: random letter generator
def index(request): 
    context ={
        "random": get_random_string(length=14)
    }
    return render(request,'app_01/index.html',context)

def random_word(request):
    if 'cnt' not in request.session:
        request.session['cnt']=0
    else:
        request.session['cnt']=request.session['cnt']+1
    return redirect('/')

def reset(request):
    del request.session['cnt']
    return redirect('/')
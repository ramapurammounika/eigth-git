from django.shortcuts import render

# Create your views here.
def second(request):
    d={'amma':'nanna','sister':'brother'}
    return render(request,'second.html',d)
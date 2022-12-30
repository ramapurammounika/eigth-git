from django.shortcuts import render

# Create your views here.
def first(request):
    d={'raja':'rani','lila':'majunu'}
    return render(request,'first.html',d)
from django.shortcuts import render

# Create your views here.
def wedding(request):
    return render(request, 'index.html', locals())

def location(request):
    return render(request, 'location.html', locals())
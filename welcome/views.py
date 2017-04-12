from django.shortcuts import render

# Create your views here.
def wedding(request):
    return render(request, 'wedding.html', {})
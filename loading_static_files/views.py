from django.shortcuts import render

# Create your views here.
def views_static(request):
    return render(request, 'index.html')

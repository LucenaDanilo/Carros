from django.shortcuts import render

# Create your views here.

def motos_view(request):
    return render(request, 'motos.html')
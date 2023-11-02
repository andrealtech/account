from django.shortcuts import render

def marcas_view(request):
    return render(request, 'marcas.html')

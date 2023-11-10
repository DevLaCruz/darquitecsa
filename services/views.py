from django.shortcuts import render
from .models import Services

def services(request):
    services = Services.objects.all()
    return render(request, 'services/services.html', {'services': services})


def home(request):
    from services.models import Services  # Importa el modelo Services desde la aplicación services
    services_data = Services.objects.all()  # Obtén todos los datos de servicios
    return render(request, 'core/home.html', {'services': services_data})

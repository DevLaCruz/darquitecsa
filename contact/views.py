from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactFrom

# Create your views here.
def contact(request):
    contact_form=ContactFrom()
    if request.method=='POST':
        contact_form= ContactFrom(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            subject=request.POST.get('subject','')
            content=request.POST.get('content','')
            #Suponiendo que todo ha ido bien
            return redirect(reverse('contact')+'?ok')

    return render(request, 'contact/contact.html', {'form':contact_form})
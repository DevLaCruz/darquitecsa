from django import forms

class ContactFrom(forms.Form):
    name=forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control form-control-lg form-control-a', 'placeholder':'Su Nombre', 'data-rule':'email', 'data-msg':'Please enter a valid email'}
    ), min_length=3, max_length=100)
    email=forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control form-control-lg form-control-a', 'placeholder':'Su Email'}
    ), min_length=3, max_length=100)
    subject=forms.EmailField(label='subject', required=True, widget=forms.TextInput(
        attrs={'class':'form-control form-control-lg form-control-a', 'placeholder':'Asunto'}
    ), min_length=3, max_length=100)
    content=forms.CharField(label='Contenido', required=True, widget=forms.TextInput(
        attrs={'class':'form-control form-control-lg form-control-a', 'placeholder':'Contenido'}
    ), min_length=3, max_length=500)
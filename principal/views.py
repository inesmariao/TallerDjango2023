from django.shortcuts import render

def inicio(request):
    titulo = "Inicio"
    nombre = "Inés María"
    context={
        "titulo": titulo,
        "nombre": nombre,
    }
    return render(request, 'index.html', context)

def contacto(request):
    titulo = "Contacto"
    context={
        "titulo": titulo,
    }
    return render(request, 'contacto.html', context)
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "home_active": "active",
        "title": "Home",
    }
    return render(request, 'home.html', context)
    
def about(request):
    context = {
        "about_active": "active",
        "title": "About",
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "contact_active": "active",
        "title": "Contact",
    }
    return render(request, 'contact.html', context)

def supermario(request):
    context = {
        "supermario_active": "active",
        "title": "Super Mario",
    }
    return render(request, 'supermario.html', context)

def doctorhyde(request):
    context = {
        "supermario_active": "active",
        "title": "Super Mario",
    }
    return render(request, 'doctorhyde.html', context)

from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "home_page": "active",
        "title": "Home",
    }
    return render(request, 'home.html', context)
    
def about(request):
    context = {
        "about_page": "active",
        "title": "About",
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        "contact_page": "active",
        "title": "Contact",
    }
    return render(request, 'contact.html', context)

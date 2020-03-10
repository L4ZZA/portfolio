from django.shortcuts import render

projectss = {
    'mario':{

    }
}
projects = [
    {
        'title':'Super Marioish',
        'type':'University',
        'description':'',
        'media_width': 575, 
        'media_height': 455,
        'media':[
            {
                'url':'https://www.youtube.com/embed/amrid966XhQ',
                'alt':'',
                'isVideo': True,
            },
            {
                'url':'images/java8-1280.jpg',
                'alt':'java8 not found',
                'isVideo': False,
            },
            {
                'url':'images/jbox2d-1280.jpg',
                'alt':'jbox2d not found',
                'isVideo': False,
            },
        ]
    },
    {
        'title':'Doctor Hyde',
        'type':'Personal',
        'description':'University',
        'media_width': 616.656,
        'media_height': 346.719,
        'media':[
            {
                'url':'https://www.youtube.com/embed/uc-cjUKcY0Y',
                'alt':'',
                'isVideo': True,
            },
            {
                'url':'images/java8-1280.jpg',
                'alt':'java8 not found',
                'isVideo': False,
            },
            {
                'url':'images/jbox2d-1280.jpg',
                'alt':'jbox2d not found',
                'isVideo': False,
            },
        ]
    },
]


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
        "project": projects[0],
    }
    return render(request, 'supermario.html', context)

def doctorhyde(request):
    context = {
        "doctorhyde_active": "active",
        "project": projects[1],
    }
    return render(request, 'doctorhyde.html', context)



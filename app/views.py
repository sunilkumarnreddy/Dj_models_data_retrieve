from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='Cricket')
    #LTO=Topic.objects.get(topic_name='Cricket')
    
    d={'LTO':LTO}
    return render(request, 'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.filter(topic_name='Volley Ball')
    LWO=Webpage.objects.exclude(topic_name='Volley Ball')
    LWO=Webpage.objects.all()[3::]
    LWO=Webpage.objects.all()[::-1]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    
    
    
    
    d={'LWO':LWO}
    return render(request, 'display_webpages.html',d)











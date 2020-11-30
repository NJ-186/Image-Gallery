from django.shortcuts import render
from .models import ImageObject, Tag

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    image_list = ImageObject.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(image_list, 8)
    
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'images': images })


def search(request):
    if request.method == 'POST':
        
        pref = request.POST['preference'].split() 
        
        tags = Tag.objects.filter(tag__in = pref)
        
        images = ImageObject.objects.filter(tag__in = tags)

        return render(request,'search.html', {'images': images })

    else:
        return render(request,'search.html')


def add(request):
    if request.method == 'POST':
        image_file = request.FILES['myfile']
        tags = request.POST['tags']

        image = ImageObject.objects.create(image_file = image_file)

        for tag in tags:
            image.tag.add = Tag.objects.filter(tag = tag)

        message = 'File successfully added'

        return render(request,'add.html', {'message': message})

    else:
        return render(request,'add.html')

def image(request,pk):
    image = ImageObject.objects.get(pk = pk)

    return render(request, 'image.html', {'image': image})
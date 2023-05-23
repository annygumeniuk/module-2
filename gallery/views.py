from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from urllib import request
import datetime


def gallery_view(request):
    # Retrieve all images from the database (e.g., last month's images)
    images = Image.objects.filter(created_date__gte=datetime.date.today() - datetime.timedelta(days=30))

    context = {
        'images': images
    }
    return render(request, 'gallery.html', context)


def image_detail(request, pk):
    # Retrieve the Image object based on the captured primary key (pk)
    image = get_object_or_404(Image, pk=pk)

    # Pass the image object to the template for rendering
    context = {'image': image}
    return render(request, 'image_detail.html', context)


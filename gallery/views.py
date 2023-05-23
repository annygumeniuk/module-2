from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from urllib import request

def gallery_view(response):
    return render(response, 'gallery.html', {})


def image_detail(request, pk):
    # Retrieve the Image object based on the captured primary key (pk)
    image = get_object_or_404(Image, pk=pk)

    # Pass the image object to the template for rendering
    context = {'image': image}
    return render(request, 'image_detail.html', context)


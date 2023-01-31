from django.shortcuts import render, HttpResponse
from .models import HomeImages, About, Reviews, Category, CategoryImages, Prices, Contact
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render
from django.http import Http404


# Create your views here.


def index(request):
    """
    Home | Index page
    """
    images = HomeImages.objects.filter().order_by('-id')
    categories = Category.objects.all()
    about_data = About.objects.last()
    return render(request, 'index.html', {'images': images, 'categories': categories, 'about_data': about_data})



def about(request):
    """
    About Page
    """
    data = About.objects.first()
    reviews = Reviews.objects.all()
    categories = Category.objects.all()
    return render(request, 'about.html', {'data': data, 'reviews': reviews,
                                        'categories': categories})



def single_category(request, name):
    """
    Images by Category | Gallery
    """
    try:
        about_data = About.objects.last()
        categories = Category.objects.all()
        category = Category.objects.get(name=name)
        images = CategoryImages.objects.filter(category=category).order_by('-id')
        length = len(images)
        return render(request, 'gallery.html', {'images': images,'category': category, 'categories': categories,
                                                 'length': length, 'about_data': about_data})
    except ObjectDoesNotExist:
        pass # 404 page



def price_page(request):
    """
    Pricing Page
    """
    about_data = About.objects.last()
    categories = Category.objects.all()
    pricing = Prices.objects.all().order_by('price')
    reviews = Reviews.objects.all()
    return render(request, 'pricing.html', {'categories': categories, 'about_data': about_data,
                                             'pricing': pricing, 'reviews': reviews})


def contact_page(request):
    """
    Contact page
    """
    categories = Category.objects.all()
    data = About.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
        messages.success(request, 'Thank you We will get back to you soon !')
        return render(request, 'contact.html', {'categories': categories, 'data': data})
    return render(request, 'contact.html', {'categories': categories, 'data': data})



def custom_404(request, exception):
    """
    404 function
    """
    return render(request, '404.html')



from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.models import HomeImages, About, Reviews, Category, CategoryImages, Prices, Contact
from django.core.exceptions import ObjectDoesNotExist
from openpyxl import Workbook


# Create your views here.


@login_required
def index(request):
    """
    Home page + Edit home page in the app
    """
    images = HomeImages.objects.all().order_by('-id')
    if request.method == 'POST' and request.FILES['img']:
        title = request.POST['title']
        img = request.FILES['img']
        if len(HomeImages.objects.all()) == 16:
            messages.error(request, 'To Much Images ! delete image for upload new')
            return render(request, 'main.html', {'images': images})
        else:
            save = HomeImages.objects.create(title=title,img=img)
            save.save()
            messages.success(request, 'Added Image')
            return render(request, 'main.html', {'images': images})
        
    return render(request, 'main.html', {'images': images})



def singin(request):
    """
    Login page | function
    """
    if request.user.is_authenticated:
        return redirect('/manage/')
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['pass']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/manage/')
        else:
            messages.error(request, 'Check more time the username or password !')
            return render(request, 'login.html')

    return render(request, 'login.html')



@login_required
def signout(request):
    """
    Logout Function
    """
    logout(request)
    return redirect('/manage/')



@login_required
def home_delete(request, id):
    """
    Delete Home Images
    """
    try:
        image = HomeImages.objects.get(id=id)
        image.delete()
        messages.success(request, 'Image deleted')
        return redirect('/manage/')
    except ObjectDoesNotExist:
        messages.error(request, 'Field to delete image !')
        return redirect('/manage/')



@login_required
def about(request):
    """
    About Page admin
    """
    data = About.objects.first()
    if request.method == 'POST':
        img = request.FILES.get('img', None)
        if img is None:
            pass
        else:
            data.img = img
        phone = request.POST['phone']
        email  = request.POST['email']
        instegram_name = request.POST['instegram']
        instegram_link = request.POST['link']
        city = request.POST['city']
        data.phone = phone
        data.email = email
        data.instegram = instegram_name
        data.instegram_link = instegram_link
        data.city = city
        data.save()
        messages.success(request, 'Data Updated !')
        return render(request, 'about_admin.html', {'data': data})

    return render(request, 'about_admin.html', {'data': data})



@login_required
def reviews(request):
    """
    Add Reviews 
    """
    data = Reviews.objects.all()
    if request.method == 'POST' and request.FILES['img']:
        name = request.POST['name']
        role = request.POST['role']
        detail  = request.POST['detail']
        img = request.FILES['img']
        save = Reviews.objects.create(name=name,role=role,detail=detail,img=img)
        save.save()
        messages.success(request, 'Added Review')
        return render(request, 'reviews.html', {'data': data})

    return render(request, 'reviews.html', {'data': data})



@login_required
def delete_review(request, id):
    """
    Delete Review
    """
    try:
        review = Reviews.objects.get(id=id)
        review.delete()
        messages.success(request, 'Review Deleted')
        return redirect('/manage/reviews')
    except ObjectDoesNotExist:
        messages.error(request, 'Error do delete review')
        return redirect('/manage/reviews')



@login_required
def category(request):
    """
    Category Admin Page
    """
    cat = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) > 15:
            messages.error(request, 'Name To Long !')
            return render(request, 'category.html', {'cat': cat})

        detail = request.POST['detail']
        save = Category.objects.create(name=name,detail=detail)
        save.save()
        messages.success(request, 'Added Category')
        return render(request, 'category.html', {'cat': cat})

    return render(request, 'category.html', {'cat': cat})



@login_required
def delete_category(request, id):
    """
    Delete Category Function
    """
    try:
        cat = Category.objects.get(id=id)
        cat.delete()
        messages.success(request, 'Deleted Category')
        return redirect('/manage/category')
    except ObjectDoesNotExist:
        messages.error('Field To Delete Category')
        return redirect('/manage/category')



@login_required
def single_gallery(request, name):
    """
    Single Gallery Page, shows all specific Gallery Images and can delete and add 
    """
    cat = Category.objects.get(name=name)
    images = CategoryImages.objects.filter(category=cat).order_by('-id')
    if request.method == 'POST' and request.FILES['img']:
        img = request.FILES['img']
        save = CategoryImages.objects.create(category=cat,img=img)
        save.save()
        messages.success(request, 'Added Image')
        return render(request, 'gallery_single.html', {'cat': cat, 'images': images})

    return render(request, 'gallery_single.html', {'cat': cat, 'images': images})



@login_required
def delete_image(request, name, id):
    """
    Delete Image from single Gallery category
    """
    try:
        image = CategoryImages.objects.get(id=id)
        image.delete()
        messages.success(request, 'Image deleted')
        return redirect(f'/manage/gallery/{name}')
    except ObjectDoesNotExist:
        messages.error(request, 'Error do delete')
        return redirect(f'/manage/gallery/{name}')



@login_required
def prices_page(request):
    """
    Prices Page | Add + Delete
    """
    prices = Prices.objects.all().order_by('-price')
    if request.method == 'POST':
        service = request.POST['service']
        price = request.POST['price']
        save = Prices.objects.create(service=service,price=price)
        save.save()
        messages.success(request, 'Added Price !')
    return render(request, 'prices.html', {'prices': prices})



@login_required
def delete_prices(request, id):
    """
    Delete One of Prices by id
    """
    try:
        price = Prices.objects.get(id=id)
        price.delete()
        messages.success(request, 'Deleted Price')
        return redirect('/manage/prices')
    except ObjectDoesNotExist:
        messages.error(request, 'Field To delete Price !')
        return redirect('/manage/price')



@login_required
def contact(request):
    """
    See Clients who submited the form
    """
    contacts = Contact.objects.all().order_by('-id')
    return render(request, 'contact_admin.html', {'contacts': contacts})



@login_required
def delete_contact(request, id):
    """
    Delete Contact dont needed
    """
    try:
        contact_delete = Contact.objects.get(id=id)
        contact_delete.delete()
        messages.success(request, 'Deleted Contact !')
        return redirect('/manage/contact')
    except ObjectDoesNotExist:
        messages.error(request, 'Field To delete contact !')
        return redirect('/manage/contact')



@login_required
def export_contact_xlsx(request):
    """
    Write Contacts To Xl File
    """
    contacts = Contact.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.append(['Name','Email','Phone','Subject','Messsge'])
    for contact in contacts:
        ws.append([contact.name,contact.email,contact.phone,contact.subject,contact.message])
    file_name = 'contacts.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    wb.save(response)
    return response





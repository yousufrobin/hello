from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("This is HomePage")
    context = {
        "name": Contact.objects.all()[0].name,
        "phone": Contact.objects.all()[0].phone,
    }
    return render(request, "index.html", context)


def about(request):
    # return HttpResponse("This is AboutPage")
    context = {"name": "Mohammad Yousuf", "age": "30", "gender": "Male"}
    return render(request, "about.html", context)


def services(request):
    # return HttpResponse("This is ServicesPage")
    return render(request, "services.html")


def contact(request):
    # return HttpResponse("This is ContactPage")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact.save()
        messages.success(request, "Your Contact From has been submitted!")
    return render(request, "contact.html")

from django.shortcuts import render
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
    students = Student.objects.all()
    if request.method == "POST":
        if "add" in request.POST:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            address = request.POST.get("address")
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                address=address
                )
            messages.success(request,"Student Added Successfully")
        
        elif request.method == "POST":
            if "add" in request.POST:
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                phone = request.POST.get("phone")
                email = request.POST.get("email")
                address = request.POST.get("address")
                Student.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    address=address
                    )
                messages.success(request,"Student Added Successfully")
                
            
    return render(request,"index.html",{"students": students})
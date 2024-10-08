from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q


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
        
        elif "update" in request.POST:
            id = request.POST.get("id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            address = request.POST.get("address")
            
            update_student = Student.objects.get(id=id)
            update_student.first_name = first_name
            update_student.last_name = last_name
            update_student.phone = phone
            update_student.email = email
            update_student.address = address
            update_student.save()
            messages.success(request,"Student Updated Successfully")
        
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            
            messages.success(request,"Deleted Successfully")
        
        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = Student.objects.filter(
                Q(first_name__icontains=query)| 
                Q(last_name__icontains=query)|
                Q(phone__icontains=query)|
                Q(email__icontains=query)|
                Q(address__icontains=query))         
                
            
    return render(request,"index.html",{"students": students})
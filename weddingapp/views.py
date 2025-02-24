from django.shortcuts import render

from weddingapp.models import studentsmodel,StudentsDetails


# Create your views here.


def index(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        age=request.POST.get('age')
        email=request.POST.get('email')

        # create an object for the student
        new_student= studentsmodel(first_name=first_name,last_name=last_name,age=age,email=email)
        new_student.save()

        # get data from the databases
    mwanafunzione = studentsmodel.objects.all()

    return render(request,'index.html',{'mwanafunzione': mwanafunzione})

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')

        students=StudentsDetails(name=name, email= email, phone_number=phone_number, address=address, dob=dob, gender=gender)
        students.save()

    return render(request,'contact.html')
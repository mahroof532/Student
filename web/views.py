from django.shortcuts import render
from . models import Student
# Create your views here.
def index(request):
    student=Student.objects.all()
    context={
        'student':student
    }
    return render(request,'index.html',context)
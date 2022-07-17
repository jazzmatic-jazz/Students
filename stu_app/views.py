from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Student
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

 
def home(request):  
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Record Added'))
            return redirect("student")
        else:
            return redirect("home")
        
        
    form = StudentForm()
    student = Student.objects.all()
    return render(request=request, template_name="home.html", context={'form':form, 'student':student})

class StudentListView(ListView):

    context_object_name = 'student_list'
    queryset = Student.objects.order_by("name")
    template_name = "student.html"

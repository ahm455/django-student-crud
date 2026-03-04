from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import studentform
from .models import student

def create_student(request):
    if request.method == 'POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved successfully!')
            return redirect('create_student')
    else:
        form=studentform()

    students = student.objects.all() 

    return render(request,'student.html',{"form":form,'students':students}) 

def edit_student(request, student_id):    
    
    student_obj = get_object_or_404(student, id=student_id)

    if request.method == "POST":
        form = studentform(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('create_student')
    else:
        form = studentform(instance=student_obj)

    return render(request, 'student.html', {'form': form})

def student_list_view(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students': students})
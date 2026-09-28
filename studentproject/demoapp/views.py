from django.shortcuts import redirect, render
from .models import Student


def home(request):
    return render(request, 'home.html', {'student_count': Student.objects.count()})


def student(request):
    error = ''
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Student.objects.create(
                name=name,
                email=request.POST.get('email', '').strip(),
                course=request.POST.get('course', '').strip(),
            )
            return redirect('student')
        error = 'Please enter a student name.'

    return render(request, 'student.html', {
        'students': Student.objects.all(),
        'error': error,
    })
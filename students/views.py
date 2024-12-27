from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Group


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)


def student_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        full_name = request.POST.get('full_name')
        group = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        if image and full_name and date_of_birth and phone_number and location:
            group = Group.objects.get(group_name=group)
            Student.objects.create(
                image=image,
                full_name=full_name,
                group=group,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                location=location,
            )
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'students/student-add.html', ctx )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        image = request.FILES.get('image')
        full_name = request.POST.get('full_name')
        group_name = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        if image and full_name and date_of_birth and phone_number and location:
            group = Group.objects.get(group_name=group_name)
            student.image=image
            student.full_name=full_name
            student.group=group
            student.date_of_birth=date_of_birth
            student.phone_number=phone_number
            student.location=location
            student.save()
            return redirect(student.get_detail_url())
    groups = Group.objects.all()
    ctx = {
            'student': student,
            'groups': groups,
           }
    return render(request, 'students/student-add.html', ctx)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')
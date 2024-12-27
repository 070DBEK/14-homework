from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers' : teachers}
    return render(request, 'teachers/teacher-list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        subject = request.POST.get('subject')
        if first_name and last_name and number and email and experience and image and subject:
            Teacher.objects.create(
                first_name = first_name,
                last_name = last_name,
                number = number,
                email = email,
                experience = experience,
                image = image,
                subject = subject,
            )
            return redirect('teachers:list')
    return render(request, 'teachers/teacher-add.html')


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        subject = request.POST.get('subject')
        if first_name and last_name and number and email and experience and image and subject:
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.number = number
            teacher.email = email
            teacher.experience = experience
            teacher.image = image
            teacher.subject = subject
            teacher.save()
            return redirect(teacher.get_detail_url())
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect('teachers:list')
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-list.html', ctx)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from subjects.models import Subject


def teachers_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)


def create_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        photo = request.FILES.get('photo')

        if all([first_name, last_name, subject_id, phone, email, experience, photo]):
            subject = Subject.objects.filter(id=subject_id).first()
            if subject:
                Teacher.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    subject=subject,
                    phone=phone,
                    email=email,
                    experience=experience,
                    photo=photo
                )
                return redirect('teachers:list')
        return redirect('teachers:create')

    subjects = Subject.objects.all()
    return render(request, 'teachers/teacher-add.html', {'subjects': subjects})


def update_teacher(request, pk):
    teacher = Teacher.objects.filter(id=pk).first()
    if not teacher:
        return redirect('teachers:list')

    if request.method == 'POST':
        # Collect form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        photo = request.FILES.get('photo')

        # Validate that all required fields are filled
        if not all([first_name, last_name, subject_id, phone, email, experience]):
            return redirect('teachers:add', pk=pk)

        # Find the subject by ID
        subject = Subject.objects.filter(id=subject_id).first()
        if not subject:
            return redirect('teachers:add', pk=pk)

        # Update teacher details
        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.subject = subject
        teacher.phone = phone
        teacher.email = email
        teacher.experience = experience

        # If a new photo is uploaded, update it
        if photo:
            teacher.photo = photo

        # Save the updated teacher
        teacher.save()

        # Redirect to the teacher list after the update
        return redirect('teachers:list')

    # Get all subjects to show in the form
    subjects = Subject.objects.all()
    return render(request, 'teachers/teacher-add.html', {'teacher': teacher, 'subjects': subjects})


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher-detail.html', {'teacher': teacher})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:list')

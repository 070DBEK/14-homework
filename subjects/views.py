from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from teachers.models import Teacher


def home(request):
    return render(request, 'index.html')


def subject_list(request):
    subjects = Subject.objects.all()
    subjects_count = subjects.count()
    ctx = {'subjects':subjects, 'subjects_count':subjects_count}
    return render(request, 'subjects/subjects-list.html', ctx)


def create_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject = Subject.objects.create(name=name)
            teacher_ids = request.POST.getlist('teachers')
            for teacher_id in teacher_ids:
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.subject = subject
                teacher.save()
            return redirect('subjects:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'subjects/subject-add.html', ctx)


def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject.name = name
            subject.save()

            # O'qituvchilarni yangilash
            teacher_ids = request.POST.getlist('teachers')

            # Get Teacher instances based on the provided IDs
            teachers = Teacher.objects.filter(id__in=teacher_ids)

            # Replace the existing teachers with the new ones
            subject.teachers.set(teachers)

            subject.save()
            return redirect('subjects:list')

    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers, 'subject': subject}
    return render(request, 'subjects/subject-add.html', ctx)


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subjects:list')


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)

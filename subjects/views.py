from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject


def home(request):
    return render(request, 'index.html')


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subject-list.html', ctx)


def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(name=name)
            return redirect('subjects:list')
    return render(request, 'subjects/subject-add.html')


def update_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject.name = name
            subject.save()  # Yangilanishni saqlashni unutmang
            return redirect(subject.get_detail_url())
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-add.html', ctx)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subjects:list')


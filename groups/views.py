from django.shortcuts import render, redirect, get_object_or_404
from .models import Group


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/group-list.html', ctx)


def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        students = request.POST.get('students')
        if name and teacher and students:
            Group.objects.create(
                name=name,
                teacher=teacher,
                students=students,
            )
            return redirect('groups:list')
    return render(request, 'groups/group-add.html')


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        students = request.POST.get('students')
        if name:
            group.name = name
            group.teacher = teacher
            group.students = students
            group.save()
            return redirect(group.get_detail_url())
    ctx = {'group': group}
    return render(request, 'groups/group-add.html', ctx)


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        group.delete()
        return redirect('groups:list')
    ctx = {'group': group}
    return render(request, 'groups/group-list.html', ctx)

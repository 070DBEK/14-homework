from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from teachers.models import Teacher
from students.models import Student
from django.contrib import messages


def groups_list(request):
    groups = Group.objects.all()
    group_count = groups.count()
    ctx = {'groups': groups, 'group_count':group_count}
    return render(request, 'groups/groups-list.html', ctx)


def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('students')

        if not name or not teacher_id:
            messages.error(request, "Guruh nomi yoki sinf rahbari tanlanmagan.")
            return redirect('groups:add')

        # Teacherni olish
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            messages.error(request, "Tanlangan o'qituvchi mavjud emas.")
            return redirect('groups:add')

        # Group yaratish
        group = Group.objects.create(name=name, teacher=teacher)

        # Agar o'quvchilar tanlangan bo'lsa, ularni qo'shing
        if student_ids:
            students = Student.objects.filter(id__in=student_ids)
            group.students.set(students)

        group.save()
        messages.success(request, "Guruh muvaffaqiyatli yaratildi.")
        return redirect('groups:list')

    teachers = Teacher.objects.all()
    students = Student.objects.all()
    ctx = {'teachers': teachers, 'students': students}
    return render(request, 'groups/group-add.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        group.delete()
        return redirect('groups:list')
    ctx = {'group': group}
    return render(request, 'groups/group-list.html', ctx)


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()
    ctx = {'group':group, 'students':students}
    return render(request, 'groups/group-detail.html', ctx)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from groups.models import Group


def students_list(request):
    students = Student.objects.all()
    students_count = students.count()
    ctx = {'students':students, 'students_count':students_count}
    return render(request, 'students/students-list.html', ctx)


def create_student(request, student_id=None):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        group_id = request.POST.get('group')
        if not all([full_name, date_of_birth, phone, address, group_id]):
            messages.error(request, "Barcha maydonlarni to'ldiring.")
            return redirect('students:create')
        group = Group.objects.filter(id=group_id).first()
        if not group:
            messages.error(request, "Tanlangan guruh topilmadi.")
            return redirect('students:create')
        if student_id:
            student = get_object_or_404(Student, pk=student_id)
            student.full_name = full_name
            student.date_of_birth = date_of_birth
            student.phone = phone
            student.address = address
            student.photo = photo if photo else student.photo
            student.group.set([group])
            student.save()
            messages.success(request, "Talaba muvaffaqiyatli yangilandi.")
        else:
            student = Student.objects.create(
                full_name=full_name,
                date_of_birth=date_of_birth,
                phone=phone,
                address=address,
                photo=photo if photo else None,
            )
            student.group.set([group])
            messages.success(request, "Talaba muvaffaqiyatli qo'shildi.")
        return redirect('students:list')
    if student_id:
        student = get_object_or_404(Student, pk=student_id)
    else:
        student = None
    groups = Group.objects.all()  # Barcha guruhlarni olish
    return render(request, 'students/student-add.html', {'groups': groups, 'student': student})


def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.success(request, "Talaba muvaffaqiyatli o'chirildi.")
    return redirect('students:list')


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    ctx = {'student':student}
    return render(request, 'students/student-detail.html', ctx)
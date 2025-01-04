from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from groups.models import Group


def students_list(request):
    students = Student.objects.all()
    students_count = students.count()
    ctx = {'students':students, 'students_count':students_count}
    return render(request, 'students/students-list.html', ctx)


def create_student(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')  # Rasmni olish
        group_id = request.POST.get('group')  # Tanlangan guruh ID

        # Maydonlarning to'liqligini tekshirish
        if not all([full_name, date_of_birth, phone_number, address, group_id]):
            messages.error(request, "Barcha maydonlarni to'ldiring.")
            return redirect('students:create')

        # Guruhni olish
        group = Group.objects.filter(id=group_id).first()
        if not group:
            messages.error(request, "Tanlangan guruh topilmadi.")
            return redirect('students:create')

        # Talabani yaratish
        student = Student.objects.create(
            full_name=full_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            address=address,
            photo=photo if photo else None,  # Rasmni tekshirish
        )

        # ManyToMany bog'lanishni o'rnatish
        student.groups.set([group])  # Guruhni talabaga bog'lash
        student.save()  # Talabani saqlash

        # Xabar yuborish va ro'yxat sahifasiga yo'naltirish
        messages.success(request, "Talaba muvaffaqiyatli qo'shildi.")
        return redirect('students:list')

    # Guruhlar ro'yxatini yuborish
    groups = Group.objects.all()
    return render(request, 'students/student-add.html', {'groups': groups})


def student_delete(request, student_id):
    # Talabani olish (agar mavjud bo'lsa)
    student = get_object_or_404(Student, pk=student_id)

    # Talabani o'chirish
    student.delete()

    # O'chirish muvaffaqiyatli bo'lsa, xabar yuborish
    messages.success(request, "Talaba muvaffaqiyatli o'chirildi.")

    # Talabalar ro'yxatiga qaytarish
    return redirect('students:list')


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    ctx = {'student':student}
    return render(request, 'students/student-detail.html', ctx)
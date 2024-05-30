from django.shortcuts import render, get_object_or_404, redirect

from registration_screen.models import User, UserType, Group


class TempStudentUser:
    def __init__(self, user, schedule_str):
        self.user = user
        self.schedule_str = schedule_str


class TempGroup:
    def __init__(self, name, schedule_str):
        self.name = name
        self.schedule_str = schedule_str


def show_students(request):
    current_user_id = request.session.get('current_user_id')
    if current_user_id:
        current_user = get_object_or_404(User, pk=current_user_id)
        students_id_list = current_user.get_students_id()

        students = User.objects.filter(id__in=students_id_list)
        schedule_str =  f"Вторник 19:00 - 20:00\n" \
                        f"Пятница 19:30 - 20:30\n" \
                        f"Суббота 17:00 - 18:00\n" \
                        f"Воскресенье 10:00 - 11:00\n"

        temp_students_list = []
        for student in students:
            temp_students_list.append(TempStudentUser(student, schedule_str))

        groups_id_list = current_user.get_groups_id()
        groups = Group.objects.filter(id__in=groups_id_list)
        return render(
            request,
            'students/students.html',
            {
                'students': temp_students_list,
                'groups': groups
            }
        )

    return redirect('login')
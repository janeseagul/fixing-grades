import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from datacenter.models import (
    Schoolkid,
    Chastisement,
    Mark,
    Lesson,
    Subject,
    Commendation,
)

COMMENDATIONS = [
    'Хорошо себя показал!',
    'Отлично справился с контрольной!',
    'Талантливо!',
    'Хорошо!',
    'Великолепно!',
    'Активно отвечал на уроке!',
    'Талантливо!',
    'Отлично!',
     'Здорово!'
]

def get_schoolkid(child: str):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print(f"Ученика с именем {child} не существует.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников, пожалуйста, уточните свой запрос.")


def fix_marks(schoolkid: Schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__lt=4).update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def get_lessons(title: str, year: str, letter: str):
    try:
        lessons = Lesson.objects.filter(
            group_letter=letter,
            year_of_study=year,
            subject=title).order_by('date')
        return lessons
    except not lessons:
        print(f'Предмет {title} не найден.')


def create_commendation(schoolkid: Schoolkid, lesson_title: str):
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter

    try:
        subject = Subject.objects.get(title=lesson_title, year_of_study=year_of_study)
        lesson = random.choice(get_lessons(subject, year_of_study, group_letter))
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            text=random.choice(COMMENDATIONS),
            created=lesson.date,
            teacher=lesson.teacher)
    except Subject.DoesNotExist:
        print(f"Предмет {lesson_title} не найден.")
    else:
        print ("Создана похвала от учителя")


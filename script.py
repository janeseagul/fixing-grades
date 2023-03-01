import django
import os
from random import choice

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Schoolkid,
    Chastisement,
    Mark,
    Lesson,
    Commendation,
)

COMMENDATIONS = choice([
    'Хорошо себя показал!',
    'Отлично справился с контрольной!',
    'Талантливо!',
    'Хорошо!',
    'Великолепно!',
    'Активно отвечал на уроке!',
    'Талантливо!',
    'Отлично!',
    'Здорово!'
])


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print(f"Ученика с именем {name} не существует.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников, пожалуйста, уточните свой запрос.")


def fix_marks(schoolkid: Schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__lt=4).update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def create_commendation(name, lesson_name):
    child = get_schoolkid(name)

    lessons = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject__title=lesson_name
    ).order_by('-date').first()

    if not lessons:
        print('Невозможно найти такой предмет')
        return
    Commendation.objects.create(text=COMMENDATIONS, created=lessons.date, schoolkid=child,
                                subject=lessons.subject, teacher=lessons.teacher)

# Проект "Дневник"

Вам необходимо заранее скачать [скрипт](https://github.com/devmanorg/e-diary)

Этот скрипт позволяет вам исправлять плохие оценки (2 и 3) по предметам, удалять замечания и добавлять благодарности от учителей в электронный дневник.

Также  вам необходима база данных школьных оценок.

## Подготовка

1. Скачайте файл `script.py`

2. Скачайте [репозиторий](https://github.com/devmanorg/e-diary), положите файл скрипта рядом с `manage.py`

3. Откройте Django shell

```bash
python manage.py shell
```

4. Импортируйте `script.py` в Django shell

```python
from script import get_schoolkid, fix_marks, remove_chastisements, create_commendation

```                        

## Пример работы скрипта

1. `get_schoolkid(kid_name)` :
    Запустите. Принимает имя ученика, которого нужно найти, и возвращает объект модели School kid из базы данных. 
Если не найдено ни одного ученика с указанным именем, выведет исключение.

```python
schoolkid = get_schoolkid('Имя ученика')
```

2. `fix_marks(schoolkid)` :
  Принимает на вход объект модели Schoolkid, находит плохие оценки (2,3) и изменяет их на 5.

```python
fix_marks(schoolkid)
```

3. `remove_chastisements(schoolkid)` :
   Запустите. Удаляет все замечания от учителей.

```python
remove_chastisements(schoolkid)
```

4. `create_commendation(kid_name, lesson_title)` :
  Принимает имя ученика, название темы урока и создает объект с
  текстом похвалы в случайный день.

```python
create_commendation(schoolkid, 'Subject Title')
```


Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

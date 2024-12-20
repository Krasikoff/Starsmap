# Starsmap ![CI](https://github.com/Krasikoff/Starsmap/actions/workflows/main.yml/badge.svg)

## Описание. 
Starsmap - это система по оценке компетенций сотрудника. Дашборд аналитики по навыкам в команде, который позволит руководителю увидеть состояние навыков в команде и поможет в развитии команды.  

## Используемые технологии.
![](https://img.shields.io/badge/Python-Version:_3.10.13-blue?logo=python&style=plastic) 
![](https://img.shields.io/badge/Django_4.2-006600?logo=python&style=plastic)
![](https://img.shields.io/badge/DRF_3.15.2-006600?logo=python&style=plastic)
![](https://img.shields.io/badge/Postgresql_15.3-black?logo=python&style=plastic)
![](https://img.shields.io/badge/UnitTest-grey?logo=python&style=plastic)
![](https://img.shields.io/badge/Docker-blue?logo=python&style=plastic)
![](https://img.shields.io/badge/Nginx-333333?logo=python&style=plastic)

## Ценность.
Дашборд сокращает руководителю время на анализ состояния команды, что позволяет эффективнее планировать развитие команды и найм сотрудников.

## ИСПОЛЬЗУЕМЫЕ ТЕРМИНЫ.
* Навык - умение/способность деятельность. В Starsmap сотрудники проходят оценку и могут посмотреть аналитику по отдельному навыку. 
* Компетенция - это набор навыков, которые нужны для выполнения задачи/цели. Компетенция уже содержит в себе навыки. Соответственно, в системе сотрудник себя оценивает исключительно по навыкам, не компетенциям. 
* Домен - это компетенция, которая включает в себя группу компетенций. 

## Уровни владения компетенциями. 
Это стандартные описания уровней владения навыками/компетенциями. Вы можете адаптировать описание под себя и свою команду.

* Не владеет – пока не приходилось сталкиваться с этим в реальных задачах.
* Начинающий (начинает изучать) -  начинает изучать тему/область/инструмент, но еще не было возможности применить на практике или применялось очень мало/точечно, нужна консультация/помощь коллег.
* Базовый (знает тему/область/инструмент на базовом уровне) – знает основы, применял на практике, может самостоятельно пользоваться в базовых случаях, точечно обращается за консультацией к коллегам.
* Уверенный -  хорошо ориентируется в теме/области/инструменте, может самостоятельно решить задачу, иногда требуется помощь эксперта в решении.
* Экспертный – знает тему/область/инструмент от и до, может самостоятельно решить любую задачу, консультирует и помогает коллегам по этому.

## Функциональные требования.
* Интерфейс должен быть в виде дашборда 
* Дашборд должен показывать как статические данные на текущий момент, так и динамические данные за период (3, 6, 12 месяцев) 
* В дашборд должны входить метрики, которые будут отображать как в статике, так и в динамике.
 - состояние навыков, 
 - сильные и пройденные оценки, 
 - состояние планов развития,
 - запросы на обучение, 
 - состояние вовлеченности сотрудников 

## Backend-решение.

Основано на артефактах хакатон Росбанк system analysis команда 3
https://docs.google.com/document/d/1zQA5ZYlVIoJGP9H_3WA1eZyfj642sPDn/edit#heading=h.gjdgxs
Предоставленных данных в XL таблице  app/data.csv
После запуска и загрузки данных получаем много вспомагательных и несколько рабочих route: choice для наполнения меню управления фильтром, filter, для возврата данных в соответствии с выбороми в меню и динамическим подсчетом вычисляемых значений, для отображения на фронтенд - количество должностей в команде, количество навыков, компетенций...
route lastrating method patch изменяет поля о потребности в обучении и дату изменения.
router candidate method post, dеlete добавляет, удаляет ссылки кандидатов на должность.

Админка настроена так,что в ней вручную (не оптимизировано) можно вести работу HR, руководителя, донастроив группы и права https://starsmap.ddns.net/admin/

## Запуск на сервере.
Протестировано на Ubuntu с поддержкой docker контейнеров. Демо на сервере:
https://starsmap.ddns.net/swagger/

для запуска на сервере заполнить файл .env переменными окружения как в примере env.example
``` shell
git clone https://github.com/Krasikoff/Starsmap
```
настроить в settings django CORS_ALLOWED_ORIGINS, ALLOWED_HOSTS
``` shell
docker-compose up -d --build
```

## Запуск локально.
- подготовка, скачиваем репозиторий
``` shell
git clone https://github.com/Krasikoff/Starsmap
```
- переходим в каталог Starsmap или открываем в любимом IDE

``` shell
python -m venv venv
source venv/bin/activate
pip install django==4.2
pip install --upgrade pip
cd app/
python manage.py makemigrations
python manage.py migrate
```
- наполняем БД, если требуется
в BASE_DIR/app должен лежать data.csv в определенном формате.
* загрузка из XL в БД
* согласование последней оценки между rating и lastrating
``` shell
python manage.py upload_data
python manage.py refresh_last_data
```
- запуск
``` shell
python manage.py runserver  
```
- создаем первого суперпользователя
``` shell
python manage.py createsuperuser
```
- для сбора статической API документации
``` shell
python3 manage.py generateschema > schema.yaml 
```
- для запуска юнит-тестов
``` shell
cd app/
python manage.py test -v 2
```

## Свагер:

локально:
http://localhost:8000/swagger/
Демо на сервере:
https://starsmap.ddns.net/swagger/

## Команда проекта:

- Product manager
Галиакбарова Карина
- Data analytics 
Дмитрий Быстров
Дмитрий Симкин
- Systems analytics
Мария Спиренкова
- Business analytics
Ксения Никитина
- Designers
Дарья Курлянова
Ольга Литова
- Backend developers
Дмитрий Красиков
Кирилл Собковский
- Frontend developers
Дмитрий Янюк

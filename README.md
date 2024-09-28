# Starsmap

## Описание. 

Starsmap - это система по оценке компетенций сотрудника. Дашборд аналитики по навыкам в команде, который позволит руководителю увидеть состояние навыков в команде и поможет в развитии команды.  

## Ценность: 

Дашборд сокращает руководителю время на анализ состояния команды, что позволяет эффективнее планировать развитие команды и найм сотрудников.

## ИСПОЛЬЗУЕМЫЕ ТЕРМИНЫ

* Навык - умение/способность деятельность. В Starsmap сотрудники проходят оценку и могут посмотреть аналитику по отдельному навыку. 
* Компетенция - это набор навыков, которые нужны для выполнения задачи/цели. Компетенция уже содержит в себе навыки. Соответственно, в системе сотрудник себя оценивает исключительно по навыкам, не компетенциям. 
* Домен - это компетенция, которая включает в себя группу компетенций. 

## Уровни владения компетенциями 

Это стандартные описания уровней владения навыками/компетенциями. Вы можете адаптировать описание под себя и свою команду.

* Не владеет – пока не приходилось сталкиваться с этим в реальных задачах.
* Начинающий (начинает изучать) -  начинает изучать тему/область/инструмент, но еще не было возможности применить на практике или применялось очень мало/точечно, нужна консультация/помощь коллег.
* Базовый (знает тему/область/инструмент на базовом уровне) – знает основы, применял на практике, может самостоятельно пользоваться в базовых случаях, точечно обращается за консультацией к коллегам.
* Уверенный -  хорошо ориентируется в теме/области/инструменте, может самостоятельно решить задачу, иногда требуется помощь эксперта в решении.
* Экспертный – знает тему/область/инструмент от и до, может самостоятельно решить любую задачу, консультирует и помогает коллегам по этому.

## Функциональные требования

* Интерфейс должен быть в виде дашборда 
* Дашборд должен показывать как статические данные на текущий момент, так и динамические данные за период (3, 6, 12 месяцев) 
* В дашборд должны входить метрики, которые будут отображать как в статике, так и в динамике.
 - состояние навыков, 
 - сильные и пройденные оценки, 
 - состояние планов развития,
 - запросы на обучение, 
 - состояние вовлеченности сотрудников 

## Запуск
- подготовка, скачиваем с гит
``` shell
git clone https://github.com/Krasikoff/Starsmap
```
- переходим в каталог Starsmap или открываем в любимом IDE

``` shell
python -m venv venv
source venv/bin/activate
pip install django==4.2
pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate
```
- наполняем БД, если требуется
в BASE_DIR должен лежать data.csv в определенном формате.
``` shell
python manage.py upload_data
```
- запуск
``` shell
python manage.py runserver  
```
- создаем первого суперпользователя
``` shell
python manage.py createsuperuser
```

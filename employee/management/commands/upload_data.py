from django.core.management.base import BaseCommand
from datetime import datetime
from starsmap.settings import BASE_DIR
from employee.models import (
    Employee,
    Position,
    Team,
    Skill,
    Competence,
    Rating,
)


class Command(BaseCommand):
    help = 'Upload to the db from XL.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount', type=int,
            help='The number of string that should be created.'
        )

    def handle(self, *args, **kwargs):
        amount = kwargs['amount'] if kwargs['amount'] else 0
        with open(f'{BASE_DIR}/data.csv', 'r') as file1:
            count = 0
            for line in file1:
                count += 1
                if count == 1:
                    title = line.split(";")
                    print(title[1], title[2],title[3],title[4])
                else:
                    if amount > 0:
                        if count > amount:
                            break
                    data = line.split(";")
                    (position, _) = Position.objects.get_or_create(name=data[2])
                    (team, _) = Team.objects.get_or_create(name=data[3])
                    try:
                        cr_date = datetime.strptime(data[13], '%d.%m.%Y')
                    except Exception as e:
                        cr_date = datetime.strptime(data[13], '%Y-%m-%d %H:%M:%S')
                    (employee, _) = Employee.objects.get_or_create(
                         fio=data[1],             
                         position=position,
                         team=team,
                         grade=data[4],
                         date_last_rating=cr_date
                    )
                    (competence, _) = Competence.objects.get_or_create(name=data[7])
                    (skill, _) = Skill.objects.get_or_create(
                        name=data[6],
                        domain=data[8],
                        competence=competence,
                    )
                    try:
                        c_date = datetime.strptime(data[5], '%d.%m.%Y')
                        u_date = datetime.strptime(data[9], '%d.%m.%Y')
                    except Exception as e:
                        c_date = datetime.strptime(data[5], '%Y-%m-%d %H:%M:%S')
                        u_date = datetime.strptime(data[9], '%Y-%m-%d %H:%M:%S')
                    if data[19] == 'да':
                        key_people = True
                    else:
                        key_people = False
                    (raiting, _) = Rating.objects.get_or_create(
                        fio=employee,                    
                        created_at=c_date,
                        updated=u_date,
                        skill=skill,
                        competence=competence,
                        rating=data[11],
                        key_people=key_people
                    )
                    print('-----------------------')    
                    print(raiting)
            print('Должностей: ', Position.objects.count())
            print('Команд: ', Team.objects.count())
            print('Сотрудников: ', Employee.objects.count())
            print('Навыков: ', Skill.objects.count())
            print('Компетенций: ', Competence.objects.count())
            print('Рейтингов: ', Rating.objects.count())
        return None

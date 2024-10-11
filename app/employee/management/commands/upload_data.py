from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from transliterate import translit

from employee.models import (Competence, LastRating, Position, Rating, Skill,
                             Team)
from starsmap.settings import BASE_DIR

User = get_user_model()


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
                    print(title[3], title[2], title[1], title[4], title[8], title[10])
                else:
                    if amount > 0:
                        if count > amount:
                            break
                    data = line.split(";")
                    (position, _) = Position.objects.get_or_create(
                        name=data[2]
                    )
                    (team, _) = Team.objects.get_or_create(name=data[3])
                    f_name = translit(data[1].split()[1], reversed=True).replace("'", '')
                    l_name = translit(data[1].split()[0], reversed=True).replace("'", '')
                    try:
                        last_date = datetime.strptime(
                            data[13], '%d.%m.%Y'
                        )
                        hire_date = datetime.strptime(data[5], '%d.%m.%Y')
                        score_date = datetime.strptime(data[9], '%d.%m.%Y')
                    except Exception:
                        last_date = datetime.strptime(
                            data[13], '%Y-%m-%d %H:%M:%S'
                        )
                        hire_date = datetime.strptime(
                            data[5], '%Y-%m-%d %H:%M:%S'
                        )
                        score_date = datetime.strptime(
                            data[9], '%Y-%m-%d %H:%M:%S'
                        )
                    (user, _) = User.objects.get_or_create(
                        username=f'{l_name}_{f_name}',
                        last_name=data[1].split()[0],
                        first_name=data[1].split()[1],
                        position=position,
                        grade=data[4],
                        date_hire=hire_date
                    )
                    if 'да' in data[19]:
                        user.key_people = True
                    user.team.add(team)
                    user.save()
                    (competence, _) = Competence.objects.get_or_create(
                        name=data[7]
                    )
                    (skill, _) = Skill.objects.get_or_create(
                        name=data[6],
                        domain=data[8],
                        competence=competence,
                    )
                    (last_rating, _) = LastRating.objects.get_or_create(
                        user=user,
                        skill=skill,
                        last_date=last_date
                    )
                    if 'да' in data[14]:
                        last_rating.last_match = True
                        last_rating.save()
                    (rating, _) = Rating.objects.get_or_create(
                        last_rating=last_rating,
                        # date=,
                        # date_start=
                        # date_end=,
                        date_score=score_date,
                        score=data[10],
                        match=True if 'да' in data[12] else False,
                        chief_proof=True if 'да' in data[21] else False,
                    )

                    print('-----------------------')
                    print(
                        team, ',', position, ',', user.grade, ',',
                        skill.domain, ',', rating,
                    )
            print('Должностей: ', Position.objects.count())
            print('Команд: ', Team.objects.count())
            print('Сотрудников: ', User.objects.count())
            print('Навыков: ', Skill.objects.count())
            print('Компетенций: ', Competence.objects.count())
            print('Рейтингов на посл.дату: ', LastRating.objects.count())
            print('Рейтингов: ', Rating.objects.count())
        return None

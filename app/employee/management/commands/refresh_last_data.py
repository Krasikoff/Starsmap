from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from employee.models import LastRating, Rating, Skill, User

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
        count = 0
        skills = Skill.objects.all()
        users = User.objects.all()
        for user in users:
            count += 1
            for skill in skills:
                lastratings = LastRating.objects.filter(user=user.id).filter(skill_id=skill.id)
                for lastrating in lastratings:
                    print(lastrating.id, lastrating.user, lastrating.skill)
                    ratings = Rating.objects.filter(last_rating=lastrating.id)
                    r_count = 0
                    for rating in ratings:
                        if not r_count:
                            print(rating.date_score, rating.score, rating.match)
                            lastrating.last_date = rating.date_score
                            lastrating.last_score = rating.score
                            lastrating.last_match = rating.match
                            lastrating.save()
                        r_count += 1
            if amount > 0:
                if count > amount:
                    break

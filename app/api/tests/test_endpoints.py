from http import HTTPStatus

from django.test import TestCase, Client

from employee.models import (
    Competence,
    Position,
    Skill,
    Team,
    User,
    Vacancy,
)


class StaticURLTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team = Team.objects.create(
            name='Тестовое название'
        )
        cls.competence = Competence.objects.create(
            name='Тестовое название'
        )
        cls.skill = Skill.objects.create(
            name='Тестовое название',
            domain='Hard Skills',
            competence=cls.competence
        )
        cls.position = Position.objects.create(
            name='Тестовое наименование'
        )
        cls.user = User.objects.create(
            first_name='Name_1',
            last_name='Surname_1',
            grade='Junior',
            key_people=False,
            bus_factor=False,
            position=cls.position
        )
        cls.user.team.set([cls.team])
        cls.vacancy = Vacancy.objects.create(
            position=cls.position,
            team=cls.team
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='HasNoName')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_home_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list_team_endpoint_exists_at_desired_location(self):
        """Эндпоинт /team/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/team/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Тестовое название",
                    "leader": None
                }
            ]
        )

    def test_team_endpoint_exists_at_desired_location(self):
        """Эндпоинт /team/{id} доступен члену команды."""
        response = self.guest_client.get('/api/v1/team/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "name": "Тестовое название",
                "leader": None
            }
        )

    def test_teammeber_endpoint_exists_at_desired_location(self):
        """Эндпоинт /teammember/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/teammember/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_competence_endpoint_exists_at_desired_location(self):
        """Эндпоинт /competence/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/competence/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Тестовое название"
                }
            ]
        )

    def test_competence_endpoint_exists_at_desired_location(self):
        """Эндпоинт /competence/{id} не доступен любому пользователю."""
        response = self.authorized_client.get('/api/v1/competence/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "name": "Тестовое название"
            }
        )

    def test_skill_endpoint_exists_at_desired_location(self):
        """Эндпоинт /skill/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/skill/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Тестовое название",
                    "domain": "Hard Skills",
                    "competence": "Тестовое название"
                }
            ]
        )

    def test_skill_endpoint_exists_at_desired_location(self):
        """Эндпоинт /skill/{id} не доступен любому пользователю."""
        response = self.authorized_client.get('/api/v1/skill/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "name": "Тестовое название",
                "domain": "Hard Skills",
                "competence": "Тестовое название"
            }
        )

    def test_rating_endpoint_exists_at_desired_location(self):
        """Эндпоинт /rating/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/rating/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_last_rating_endpoint_exists_at_desired_location(self):
        """Эндпоинт /lastrating/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/lastrating/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list_user_endpoint_exists_at_desired_location(self):
        """Эндпоинт /user/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/user/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_endpoint_exists_at_desired_location(self):
        """Эндпоинт /user/{id} не доступен любому пользователю."""
        response = self.authorized_client.get('/api/v1/user/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()['id'], 1)
        self.assertEqual(response.json()['first_name'], 'Name_1')
        self.assertEqual(response.json()['last_name'], 'Surname_1')
        self.assertEqual(response.json()['position'], 'Тестовое наименование')
        self.assertEqual(response.json()['bus_factor'], False)
        self.assertEqual(response.json()['key_people'], False)

    def test_candidate_endpoint_exists_at_desired_location(self):
        """Эндпоинт /candidate/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/candidate/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list_vacancy_endpoint_exists_at_desired_location(self):
        """Эндпоинт /vacancy/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/vacancy/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_vacancy_endpoint_exists_at_desired_location(self):
        """Эндпоинт /vacancy/{id} не доступен любому пользователю."""
        response = self.authorized_client.get('/api/v1/vacancy/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list_position_endpoint_exists_at_desired_location(self):
        """Эндпоинт /position/ доступен любому пользователю."""
        response = self.guest_client.get('/api/v1/position/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "name": "Тестовое наименование",
                    "users_count": 1
                }
            ]
        )

    def test_position_endpoint_exists_at_desired_location(self):
        """Эндпоинт /position/{id} не доступен любому пользователю."""
        response = self.authorized_client.get('/api/v1/position/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            response.json(),
            {
                "name": "Тестовое наименование",
                "users_count": 1
            }
        )

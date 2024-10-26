from django.test import TestCase
from employee.models import Position, Team, User


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.position = Position.objects.create(name='position_1')
        cls.team = Team.objects.create(name='team_1')
        cls.user = User.objects.create(
            first_name='Name_1',
            last_name='Surname_1',
            grade='Junior',
            key_people=False,
            bus_factor=False,
            position=cls.position
        )
        cls.user.team.set([cls.team])

    def test_team_position_labels(self):
        """verbose_name поля name совпадает с ожидаемым."""
        position = EmployeeModelTest.position
        team = EmployeeModelTest.team
        verbose_position = position._meta.get_field('name').verbose_name
        verbose_team = team._meta.get_field('name').verbose_name
        self.assertEqual(verbose_position, 'Наименование')
        self.assertEqual(verbose_team, 'Наименование')

    def test_user_labels(self):
        """verbose_name полей user совпадает с ожидаемым."""
        user = EmployeeModelTest.user
        first_name = user._meta.get_field('first_name').verbose_name
        last_name = user._meta.get_field('last_name').verbose_name
        date_hire = user._meta.get_field('date_hire').verbose_name
        date_fire = user._meta.get_field('date_fire').verbose_name
        grade = user._meta.get_field('grade').verbose_name
        position = user._meta.get_field('position').verbose_name
        team = user._meta.get_field('team').verbose_name
        role = user._meta.get_field('role').verbose_name
        self.assertEqual(first_name, 'Имя')
        self.assertEqual(last_name, 'Фамилия')
        self.assertEqual(date_hire, 'Принят')
        self.assertEqual(date_fire, 'Уволен')
        self.assertEqual(grade, 'Уровень')
        self.assertEqual(position, 'Должность')
        self.assertEqual(team, 'Команда')
        self.assertEqual(role, 'Роль')

    def test_object_name_is_title_fild(self):
        """
        __str__  user - это строчка с содержимым
        user.first_name, user.last_name.
        """
        user = EmployeeModelTest.user
        expected_object_name = user.last_name + ' ' + user.first_name
        self.assertEqual(expected_object_name, str(user))
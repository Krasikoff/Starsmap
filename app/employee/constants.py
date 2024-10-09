MONTH = {
    0: 'На сегодня', 1: 'За 3 месяца', 2: 'За 6 месяца', 3: 'За 12 месяцев'
}
RATING = [
    (0, 'Не оценивался'),
    (1, 'Не владеет'),
    (2, 'Начинающий'),
    (3, 'Базовый'),
    (4, 'Уверенный'),
    (5, 'Экспертный'),
]

GRADE = [
    ('No value', 'No value'),
    ('Junior', 'Junior'),
    ('Middle', 'Middle'),
    ('Senior', 'Senior'),
]

DOMAIN = [
    ('Hard skills', 'Hard skills'),
    ('Soft skills', 'Soft skills'),
]

ADMIN = 'admin'
HR = 'hr'
TEAM_CHIEF = 'team_chief'
USER = 'user'

ROLE_CHOICES = (
    (ADMIN, 'Администратор'),
    (HR, 'HR'),
    (TEAM_CHIEF, 'Руководитель'),
    (USER, 'Пользователь')
)

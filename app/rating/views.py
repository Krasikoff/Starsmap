from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404, render
from employee.models import LastRating, Team

User = get_user_model()


def rating_detail(request, pk):
    # период задаем
    start_date = datetime.strptime('30.09.2023', '%d.%m.%Y')
    end_date = datetime.strptime('30.12.2023', '%d.%m.%Y')

    # TO DO переделать рейтинг в цифровой. (и в upload).

    employee = get_object_or_404(User, pk=pk)
    rating_lines = get_list_or_404(LastRating.objects.filter(
        Q(user_id=pk) 
#        &
#        Q(updated__gt=start_date) & Q(updated__lt=end_date)
    )
    )
    template = 'rating/detail.html'
    context = {'rating_lines': rating_lines, 'employee': employee}
    return render(request, template, context)


def rating_list(request):
    rating_catalog = get_list_or_404(User, is_superuser=False)
    for line in rating_catalog:
        teams = Team.objects.filter(user__id=line.id)
        for team in teams:
            line.teamname = team
    template = 'rating/list.html'
    context = {'rating_list': rating_catalog,}
    return render(request, template, context)

from django.shortcuts import(
    get_list_or_404, get_object_or_404, render
)
from employee.models import Employee


rating_catalog = get_list_or_404(Employee)


def rating_detail(request, pk):
    line = get_object_or_404(Employee, pk=pk)
    template = 'rating/detail.html'
    context = {'rating': line}
    return render(request, template, context)


def rating_list(request):
    template = 'rating/list.html'
    context = {'rating_list': rating_catalog}
    return render(request, template, context)

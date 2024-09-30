from django.shortcuts import(
    get_list_or_404, get_object_or_404, render
)
from employee.models import Employee, Rating



def rating_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    rating_lines = get_list_or_404(Rating.objects.filter(fio=pk))
    template = 'rating/detail.html'
    context = {'rating_lines': rating_lines, 'employee': employee}
    return render(request, template, context)


def rating_list(request):
    rating_catalog = get_list_or_404(Employee)
    template = 'rating/list.html'
    context = {'rating_list': rating_catalog}
    return render(request, template, context)

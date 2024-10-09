# from django_filters.rest_framework import filters


# class F(FilterSet):
#     """Filter for User by if given user_id or not"""
#     published = filters.CharFilter(field_name='id', method='filter_published')

#     def filter_published(self, queryset, name, value):
#         # construct the full lookup expression.
#         lookup = '__'.join([name, 'isnull'])
#         return queryset.filter(**{lookup: False})

#         # alternatively, you could opt to hardcode the lookup. e.g.,
#         # return queryset.filter(published_on__isnull=False)

#     class Meta:
#         model = Book
#         fields = ['published']


# # Callables may also be defined out of the class scope.
# def filter_not_empty(queryset, name, value):
#     lookup = '__'.join([name, 'isnull'])
#     return queryset.filter(**{lookup: False})

# class F(FilterSet):
#     """Filter for Books by if books are published or not"""
#     published = BooleanFilter(field_name='published_on', method=filter_not_empty)

#     class Meta:
#         model = Book
#         fields = ['published']
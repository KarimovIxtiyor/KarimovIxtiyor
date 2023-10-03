# from  django_filters import  rest_framework as filters
# from .models import Movie
#
# class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
#     pass
#
#
# class MovieFilter(filters.FilterSet):
#     genre=CharFilterInFilter(field_name='genre',lookup_expr='in')
#
#     class Meta:
#         model=Movie
#         fields=['genres']
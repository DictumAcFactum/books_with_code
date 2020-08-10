from django_filters import DateTimeFilter, AllValuesFilter, NumberFilter, FilterSet

from .models import Competition


class CompetitionFilter(FilterSet):
    from_achievement_date = DateTimeFilter(field_name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = DateTimeFilter(field_name='distance_achievement_date', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='gte')
    max_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='lte')
    drone_name = AllValuesFilter(field_name='drone__name')
    pilot_name = AllValuesFilter(field_name='pilot__name')

    class Meta:
        model = Competition
        fields = []

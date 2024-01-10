from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'time_in': ['gt'],
            'choice_types': ['exact'],
        }

# В классе
# creation_date = DateFilter(
#         field_name='creation_date',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         lookup_expr='date__gte',
#     )

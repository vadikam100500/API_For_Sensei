from django.db.models import Sum
from rest_framework.generics import ListAPIView

from .filters import MyFilter
from .models import Shop
from .pagination import ShopPagination
from .serializers import ShopSerializer


class ShopView(ListAPIView):
    serializer_class = ShopSerializer
    pagination_class = ShopPagination
    filter_backends = [MyFilter, ]
    ordering_fields = ['earnings', ]

    def get_queryset(self):
        queryset = Shop.objects.all()
        shows = self.request.query_params.getlist('show')
        groups = self.request.query_params.getlist('group')
        if shows:
            queryset = queryset.values_list(*shows)
        if groups:
            queryset = (
                queryset
                .values(*groups)
                .annotate(**{show: Sum(show) for show in shows})
            )
        if not shows and not groups:
            queryset = queryset.values_list(
                *[field.name for field in Shop._meta.get_fields()]
            )
        return queryset

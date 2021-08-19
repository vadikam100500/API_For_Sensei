from rest_framework.filters import OrderingFilter


class MyFilter(OrderingFilter):
    ordering_param = 'o'
    ordering_title = ('o')

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        start_point = request.query_params.get('date_from')
        end_point = request.query_params.get('date_to')

        if start_point:
            queryset = queryset.filter(date__gte=start_point)
        if end_point:
            queryset = queryset.filter(date__lte=end_point)
        if ordering:
            return queryset.order_by(*ordering)
        return queryset

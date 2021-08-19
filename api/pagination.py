from rest_framework.pagination import LimitOffsetPagination


class ShopPagination(LimitOffsetPagination):
    default_limit = 10

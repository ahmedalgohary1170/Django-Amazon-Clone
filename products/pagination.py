from rest_framework.pagination import PageNumberPagination


class Mypagination(PageNumberPagination):
    page_size = 10
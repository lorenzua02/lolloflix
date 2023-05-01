from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    # TODO just to test purposes, edit with correct "items per page" number
    page_size = 2

from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class ContentPaginator(PageNumberPagination):
    page_size = 10


class QuestionPaginator(Paginator):
    page_size = 5

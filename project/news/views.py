from rest_framework import generics
from .models import New
from .serializer import NewsListSerializer

from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size = 10

class NewsListAPIView(generics.ListCreateAPIView):
    queryset = New.objects.all().order_by('-id')
    serializer_class = NewsListSerializer
    pagination_class = CustomPaginator
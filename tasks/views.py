from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TaskSerialize
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .models import Task
from django.shortcuts import get_object_or_404
from rest_framework import status
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerialize
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Sorting by date (ascending order)
        sort_by_date = self.request.query_params.get('sort_by_date')
        if sort_by_date == 'true':
            queryset = queryset.order_by('created_at')  # Ensure sorting by created_at date

        # Search by date (filter tasks by date)
        search_date = self.request.query_params.get('search_date')
        if search_date:
            parsed_date = parse_date(search_date)
            if parsed_date:
                queryset = queryset.filter(created_at__date=parsed_date)

        return queryset

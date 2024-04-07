
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from citysound.tours.models import Tour
from citysound.users.models import User

from .serializers import TourSerializer

class TourViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Tour.objects.all()
        location = self.request.query_params.get('created_by', None)
        name = self.reqeust.query_params.get('name', None)

        if location:
            queryset = queryset.filter(location=location)
        if created_by_name:
            # Search Iduser from nameuser
            queryset = queryset.filter(created_by_id=user.id)
        if name:
            queryset = queryset.filter(name=name)

        return queryset
from rest_framework import generics, permissions
from rest_framework.response import Response
from sections import paginators, models
from sections import permissions as section_pemissions
from sections.serializers import content, sections

class ListAPIView(generics.ListAPIView):
    serializer_class = sections.ListSerializer
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = paginators.Paginator

class CreateAPIView(generics.CreateAPIView):
    serializer_class = sections.SectionSerializer
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser | section_pemissions.IsModerator)


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
                          permissions.IsAdminUser or section_pemissions.IsModerator)

class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class UpdateAPIView(generics.UpdateAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser or section_pemissions.IsModerator)

class DestroyAPIView(generics.DestroyAPIView):
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser or section_pemissions.IsModerator)
from rest_framework import generics, permissions
from rest_framework.response import Response
from sections import paginators, models
from sections import permissions as section_pemissions
from sections.serializers import content, sections

admin_or_mod = (permissions.IsAuthenticated,
                permissions.IsAdminUser or
                section_pemissions.IsModerator)

class ListAPIView(generics.ListAPIView):
    serializer_class = sections.ListSerializer
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = paginators.Paginator

class CreateAPIView(generics.CreateAPIView):
    serializer_class = sections.SectionSerializer
    permission_classes = admin_or_mod

class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class UpdateAPIView(generics.UpdateAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    permission_classes = admin_or_mod

class DestroyAPIView(generics.DestroyAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    permission_classes = admin_or_mod

class ContentListAPIView(generics.ListAPIView):
    serializer_class = content.ContentListSerializer
    queryset = models.SectionContent.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = paginators.ContentPaginator

class ContentCreateAPIView(generics.CreateAPIView):
    serializer_class = content.AllFieldsSerializer
    permission_classes = admin_or_mod

class ContentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

class ContentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    permission_classes = admin_or_mod

class ContentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    permission_classes = admin_or_mod

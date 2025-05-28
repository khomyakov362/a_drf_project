from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from sections import models


class AllFieldsSerializer(ModelSerializer):
    class Meta:
        model = models.SectionContent
        fields = '__all__'


class IdTitleSerializer(ModelSerializer):
    class Meta:
        model = models.SectionContent
        fields = ('id', 'title')


class ContentListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=models.Section.objects.all())

    class Meta:
        model = models.SectionContent
        fields = ('id', 'section', 'title')

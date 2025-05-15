from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from sections import models
from sections.serializers import content

class SectionSerializer(ModelSerializer):
    class Meta:
        model = models.Section
        fields = '__all__'

class ListSerializer(ModelSerializer):
    content_title = SerializerMethodField()

    def get_content_title(self, section):
        return content.IdTitleSerializer(models.SectionContent.objects.filter(section=section), many=True).data
    
    class Meta:
        model = models.Section
        fields = ('id', 'title', 'content_title')


from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections import models

class QuestionListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=models.Section.objects.all())

    class Meta:
        model = models.Question
        fields = ('id', 'section')

class QuestionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=models.Section.objects.all())

    class Meta:
        model = models.Question
        fields = ('id', 'section', 'question')
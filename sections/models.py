from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import NULLABLE

class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), **NULLABLE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')
        ordering = ['id',]

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('section'))
    title = models.CharField(max_length=150, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = _('section content')
        verbose_name_plural = _('section contents')
        ordering = ['id',]
    
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('section'))
    description = models.TextField(verbose_name=_('description'), **NULLABLE)
    question = models.TextField(verbose_name=_('question'), **NULLABLE)
    answer = models.TextField(verbose_name=_('answer'), **NULLABLE)
    """Must contain a string with a list of answers devided by ';'."""

    def __str__(self):
        return f'Question from {self.section} section about {self.answer}.'
    
    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ['section',]

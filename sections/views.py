from rest_framework import generics, permissions
from rest_framework.response import Response
from sections import paginators, models
from sections import permissions as section_pemissions
from sections.serializers import content, sections, questions

ADMIN_OR_MOD = (permissions.IsAuthenticated,
                permissions.IsAdminUser or
                section_pemissions.IsModerator)
AUTHENTICATED = (permissions.IsAuthenticated,)

class ListAPIView(generics.ListAPIView):
    serializer_class = sections.ListSerializer
    queryset = models.Section.objects.all()
    # permission_classes = AUTHENTICATED
    pagination_class = paginators.Paginator

class CreateAPIView(generics.CreateAPIView):
    serializer_class = sections.SectionSerializer
    # permission_classes = ADMIN_OR_MOD

class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    # permission_classes = AUTHENTICATED

class UpdateAPIView(generics.UpdateAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    # permission_classes = ADMIN_OR_MOD

class DestroyAPIView(generics.DestroyAPIView):
    serializer_class = sections.SectionSerializer
    queryset = models.Section.objects.all()
    # permission_classes = ADMIN_OR_MOD

class ContentListAPIView(generics.ListAPIView):
    serializer_class = content.ContentListSerializer
    queryset = models.SectionContent.objects.all()
    # permission_classes = AUTHENTICATED
    pagination_class = paginators.ContentPaginator

class ContentCreateAPIView(generics.CreateAPIView):
    serializer_class = content.AllFieldsSerializer
    # permission_classes = ADMIN_OR_MOD

class ContentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    # permission_classes = AUTHENTICATED

class ContentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    # permission_classes = ADMIN_OR_MOD

class ContentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = content.AllFieldsSerializer
    queryset = models.SectionContent.objects.all()
    # permission_classes = ADMIN_OR_MOD

class QuestionListAPIView(generics.ListAPIView):
    serializer_class = questions.QuestionListSerializer
    queryset = models.Question.objects.all()
    pagination_class = paginators.QuestionPaginator
    # permission_classes = AUTHENTICATED

class QuestionRestrieveAPIView(generics.RetrieveAPIView):
    serializer_class = questions.QuestionSerializer
    queryset = models.Question.objects.all()
    # permission_classes = AUTHENTICATED

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        the_question = models.Question.objects.get(id=pk)
        answers_str = the_question.answer
        answer_list = answers_str.split(';')
        normalized_list = list(map(lambda el: el.strip().lower(), answer_list))
        user_answer = request.data.get('user_aswer').strip().lower()
        
        is_correct = user_answer in normalized_list
        return Response({'is_correct': is_correct, 'possible_answers': normalized_list})


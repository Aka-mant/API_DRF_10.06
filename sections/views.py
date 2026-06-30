from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from sections.models import Section, Content, Question
from sections.permitions import IsModerator, IsSuperuser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentListSerializer
from sections.serializers.question_serializers import QuestionSerializer
from sections.paginators import SectionPagination, ContentPagination, QuestionPagination


class SectionListAPIView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SectionPagination


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser | IsModerator]


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsSuperuser | IsModerator]


class SectionDeleteAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsSuperuser]


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContentPagination


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, IsSuperuser | IsModerator]


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated, IsSuperuser | IsModerator]


class ContentDeleteAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsSuperuser]


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = QuestionPagination


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1]
        answer = answer.title.strip().lower()
        member_answer = request.data.get('member_answer').strip().lower()
        is_correct = member_answer == answer
        return Response({'is_correct': is_correct})

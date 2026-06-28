from rest_framework import request
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from sections.models import Section, Content
from sections.permitions import IsModerator, IsSuperuser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentListSerializer, ContentSectionSerializer

from sections.paginators import SectionPagination, ContentPagination

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
    permission_classes = [IsAuthenticated, IsSuperuser | IsModerator]



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
    permission_classes = [IsAuthenticated, IsSuperuser]



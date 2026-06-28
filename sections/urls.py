from os import path as p

from django.urls import path

from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig

from sections.views import SectionCreateAPIView, SectionRetrieveAPIView, SectionUpdateAPIView, SectionDeleteAPIView, SectionListAPIView, ContentListAPIView, ContentCreateAPIView, ContentRetrieveAPIView, ContentUpdateAPIView, ContentDeleteAPIView

app_name = SectionsConfig.name

router = DefaultRouter()

sections = 'sections/'
content = 'content/'
create = 'create/'
retrieve = 'retrieve/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'


urlpatterns = [
    # sections urlspatterns
    path(p.join(sections), SectionListAPIView.as_view(), name='section_list'),
    path(p.join(sections, create), SectionCreateAPIView.as_view(), name='section_create'),
    path(p.join(sections, int_pk), SectionRetrieveAPIView.as_view(), name='section_detail'),
    path(p.join(sections, int_pk, update), SectionUpdateAPIView.as_view(), name='section_update'),
    path(p.join(sections, int_pk, delete), SectionDeleteAPIView.as_view(), name='section_delete'),
    # content urlspatterns
    path(p.join(content), ContentListAPIView.as_view(), name='content_list'),
    path(p.join(content, create), ContentCreateAPIView.as_view(), name='content_create'),
    path(p.join(content, int_pk), ContentRetrieveAPIView.as_view(), name='content_detail'),
    path(p.join(content, int_pk, update), ContentUpdateAPIView.as_view(), name='content_update'),
    path(p.join(content, int_pk, delete), ContentDeleteAPIView.as_view(), name='content_delete'),

] + router.urls

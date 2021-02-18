# -*- coding: utf-8 -*-

from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/dcc/
    path('', views.get_user, name='front'),
    # ex: /polls/dcc/5
    path('access/<str:userListedString>/', views.access, name='access'),
    # ex: /polls/dcc/5
    path('access/<str:userListedString>/xmltohttp/', views.xmltohttp, name='xmltohttp')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
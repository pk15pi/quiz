from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from rest_framework import viewsets

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = questionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = answerSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = subjectSerializer

class questionAnswerViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = questionAnswerSerializer
    Pagination_classes = PageNumberPagination

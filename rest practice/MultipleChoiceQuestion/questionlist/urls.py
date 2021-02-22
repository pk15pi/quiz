from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'quiz', questionAnswerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
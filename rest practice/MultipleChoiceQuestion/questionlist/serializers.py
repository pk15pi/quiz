from rest_framework.response import Response

from .models import *
from rest_framework import serializers, generics, status


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'


class answerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields= ['answer','is_correct']


class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['question','id','subject_id']


class questionAnswerSerializer(serializers.ModelSerializer):
    choices = answerSerializer(many=True, read_only=False)
    class Meta:
        model=Question
        fields=['id','question','subject_id', 'choices']

    def create(self, validated_data):
        AnswerOptions = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for option in AnswerOptions:
            Answer.objects.create(question_id=question, **option)
        return question

    def update(self, instance, validated_data):
        AnswerOptions = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for option in AnswerOptions:
            Answer.objects.create(question_id=question, **option)
        return question


    '''
    def blankrecords(self, request):
        queryset=Answer.objects.filter(answer='')
        return queryset
    '''
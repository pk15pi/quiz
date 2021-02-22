from django.db import models

class Subject(models.Model):
    subject=models.CharField(max_length=50)
    def __str__(self):
        return self.subject

class Question(models.Model):
    question=models.CharField(max_length=500)
    subject_id=models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question_id=models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    answer=models.CharField(max_length=100, blank=False, null=False)
    is_correct=models.BooleanField(default=False)
    def __str__(self):
        return self.answer
    



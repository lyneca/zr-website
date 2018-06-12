from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField("Question")
    answer = models.TextField("Answer")
    answerer = models.TextField("Answerer")
    submitter = models.TextField("Submitter")
    datetime = models.DateTimeField("Date submitted", auto_now=True)

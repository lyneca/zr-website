from django.db import models

# Create your models here.

class Answer(models.Model):
    name = models.CharField("Name", max_length=50)
    text = models.TextField("Answer")
    date = models.DateTimeField("Date submitted", auto_now=True)

    def datestr(self):
        return "{}:{} • {}-{}-{}".format(
                self.date.hour,
                self.date.minute,
                *self.date.isocalendar(),
                )


    def __str__(self):
        return "{}'s answer to \"{}\"".format(self.name, Question.objects.get(answer=self.id).title)

class Question(models.Model):
    name = models.CharField("Name", max_length=50)
    title = models.CharField("Title", max_length=80)
    text = models.TextField("Question")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField("Date submitted", auto_now=True)

    def datestr(self):
        return "{}:{} • {}-{}-{}".format(
                self.date.hour,
                self.date.minute,
                *self.date.isocalendar(),
                )

    def __str__(self):
        return "{} - {}".format(self.title, self.name)


from django.db import models


class Quiz(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_questions(self):
        return self.question.all()


class Question(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        null=True,
        related_name='question'
    )

    def __str__(self):
        return self.title

    def get_answers(self):
        return self.answer.all()


class Answer(models.Model):
    title = models.CharField(max_length=50)
    right = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question,
        related_name='answer',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

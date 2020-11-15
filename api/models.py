from django.db import models

# Create your models here.

POSITIONS = (
    ('NEBULA', 'N'),
    ('GAMORA', 'G'),
    ('LOKI', 'L'),
    ('ROCKET', 'R'),
    ('HULK', 'H'),
    ('THOR', 'T'),
    ('CAP', 'Q'),
    ('BUCKY', 'B')
)

PLAYS = (
    ('90', '90'),
    ('92', '92'),
    ('93', '93'),
    ('96', '96'),
)

class Question(models.Model):
    title = models.CharField(max_length=100, null=True)
    q_text = models.CharField(max_length=250, help_text="Enter the question that you want displayed",
                        verbose_name='Question', null=True)
    q_pos = models.CharField(max_length=25, choices=POSITIONS, null=True)
    q_num = models.CharField(max_length=25, choices=PLAYS, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Question"
        verbose_name_plural = "Questions"

class Answer(models.Model):
    title = models.CharField(max_length=25, null=True)
    a_pos = models.CharField(max_length=25, choices=POSITIONS, null=True)
    a_num = models.CharField(max_length=25, choices=PLAYS, null=True)

    play = models.ImageField(upload_to="answers/", default='default.png', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Answer"
        verbose_name_plural = "Answers"

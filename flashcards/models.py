from django.db import models


# Create your models here.
class FlashCard(models.Model):
    word = models.CharField(max_length=100)
    part = models.CharField(max_length=100, choices=[('n.', 'noun'), ('v.', 'verb'), ('adj', 'adjective')])
    definition = models.TextField()
    example = models.TextField()
    collocation = models.CharField(max_length=250)

    def __str__(self):
        return self.word
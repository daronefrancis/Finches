from django.db import models

class Workout(models.Model):
  name = models.CharField(max_length=100)
  focus = models.CharField(max_length=100)
  duration = models.IntegerField()
  difficulty = models.CharField(max_length=15)
  description = models.TextField(max_length=250)

  def __str__(self):
      return self.name


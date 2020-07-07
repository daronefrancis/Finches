from django.db import models
from django.urls import reverse
from datetime import date


BODY_PARTS = (
  ('C', 'Chest'),
  ('B', 'Back'),
  ('S', 'Shoulders'),
  ('A', 'Arms'),
  ('L', 'Legs'),
  ('O', 'Cardio'),
)

class Equipment(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('equipment_detail', kwargs={'pk': self.id})

class Workout(models.Model):
  name = models.CharField(max_length=100)
  focus = models.CharField(max_length=100)
  duration = models.IntegerField()
  difficulty = models.CharField(max_length=15)
  description = models.TextField(max_length=250)
  equipment = models.ManyToManyField(Equipment)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'workout_id': self.id})
    

  def exercised_for_today(self):
    counting = 0
    for work in Workout.objects.all():
      if work.exercise_set.filter(date=date.today()):
        counting += 1
    return counting >= 1


class Exercise(models.Model):
  date = models.DateField('workout date')
  body_part = models.CharField(
    max_length=1,
    choices=BODY_PARTS
  )
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_body_part_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Workout, Equipment
from .forms import ExerciseForm

class WorkoutCreate(CreateView):
  model = Workout
  fields = '__all__'

class WorkoutUpdate(UpdateView):
  model = Workout
  fields = '__all__'

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def workouts_index(request):
  workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  equipment_workout_doesnt_have = Equipment.objects.exclude(id__in = workout.equipment.all().values_list('id'))
  exercise_form = ExerciseForm()
  return render(request, 'workouts/detail.html', { 'workout': workout, 'exercise_form': exercise_form, 'equipment': equipment_workout_doesnt_have })


def exercised(request, workout_id):
  form = ExerciseForm(request.POST)
  if form.is_valid():
    new_exercised = form.save(commit=False)
    new_exercised.workout_id = workout_id
    new_exercised.save()
  return redirect('detail', workout_id=workout_id)

def assoc_equipment(request, workout_id, equipment_id):
  Workout.objects.get(id=workout_id).equipment.add(equipment_id)
  return redirect('detail', workout_id=workout_id)

class EquipmentList(ListView):
  model = Equipment

class EquipmentDetail(DetailView):
  model = Equipment

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentUpdate(UpdateView):
  model = Equipment
  fields = ['name', 'color']

class EquipmentDelete(DeleteView):
  model = Equipment
  success_url = '/equipment/'
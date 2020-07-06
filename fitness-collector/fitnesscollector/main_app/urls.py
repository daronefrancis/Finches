from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('workouts/', views.workouts_index, name='index'),
  path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
  path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
  path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
  path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
  path('workouts/<int:workout_id>/exercised/', views.exercised, name='exercised'),
  path('workouts/<int:workout_id>/assoc_equipment/<int:equipment_id>/', views.assoc_equipment, name='assoc_equipment'),
  path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
  path('equipment/', views.EquipmentList.as_view(), name='equipment_index'),
  path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
  path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
  path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]
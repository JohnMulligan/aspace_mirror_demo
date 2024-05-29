from django.urls import path
from recordkeeper import views

urlpatterns = [
    path('records/', views.records_list),
]

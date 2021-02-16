from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterApi.as_view()),
    path('data/', views.DataView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('question-list/', views.questionList, name="question-list"),
    path('question-detail/<str:pk>/', views.questionDetail, name="question-detail"),
    path('question-create/', views.questionCreate, name="question-create"),
    path('question-update/<str:pk>/', views.questionUpdate, name="question-update"),
    path('question-delete/<str:pk>/', views.questionDelete, name="question-delete"),
    path('answer-list/', views.answerList, name="answer-list"),
    path('answer-detail/<str:pk>/', views.answerDetail, name="answer-detail"),
    path('answer-create/', views.answerCreate, name="answer-create"),
    path('answer-update/<str:pk>/', views.answerUpdate, name="answer-update"),
    path('answer-delete/<str:pk>/', views.answerDelete, name="answer-delete"),
]

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer, AnswerSerializer

from .models import Question, Answer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Question List': '/question-list/',
        'Question Detail View': '/question-update/<str:pk>/',
        'Question Create': '/question-create/',
        'Question Update': '/question-update/<str:pk>/',
        'Question Delete': '/question-delete/<str:pk>/',
        'Answer List': '/answer-list/',
        'Answer Detail View': '/answer-detail/<str:pk>/',
        'Answer Create': '/answer-create/',
        'Answer Update': '/answer-update/<str:pk>/',
        'Answer Delete': '/answer-delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def questionList(request):
    questions = Question.objects.all().order_by('title')
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def questionDetail(request, pk):
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def questionCreate(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def questionUpdate(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(instance=question, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def questionDelete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()

    return Response('Question was successfully deleted!')

@api_view(['GET'])
def answerList(request):
    answers = Answer.objects.all().order_by('title')
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def answerDetail(request, pk):
    answers = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(answers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def answerCreate(request):
    serializer = AnswerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def answerUpdate(request, pk):
    answer = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(instance=answer, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def answerDelete(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()

    return Response('This answer was successfully deleted!')

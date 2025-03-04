from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg, Max
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer

# Student Endpoints
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Test Endpoints
class TestListCreate(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestRetrieve(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

# Test Result Endpoints
class TestResultListCreate(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

@api_view(['GET'])
def student_results(request, student_id):
    results = TestResult.objects.filter(student_id=student_id)
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def test_results(request, test_id):
    results = TestResult.objects.filter(test_id=test_id)
    serializer = TestResultSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def test_average_score(request, test_id):
    avg_score = TestResult.objects.filter(test_id=test_id).aggregate(Avg('score'))
    return Response({'average_score': avg_score['score__avg']})

@api_view(['GET'])
def test_highest_score(request, test_id):
    highest_score = TestResult.objects.filter(test_id=test_id).aggregate(Max('score'))
    return Response({'highest_score': highest_score['score__max']})

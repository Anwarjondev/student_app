from django.urls import path
from .views import (
    StudentListCreate, StudentRetrieveDelete,
    TestListCreate, TestRetrieve,
    TestResultListCreate, student_results, test_results,
    test_average_score, test_highest_score
)

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='create-student'),
    path('students/<int:pk>/', StudentRetrieveDelete.as_view(), name='get-student'),
    path('tests/', TestListCreate.as_view(), name='create-test'),
    path('tests/<int:pk>/', TestRetrieve.as_view(), name='get-test'),
    path('results/', TestResultListCreate.as_view(), name='submit-test'),
    path('results/student/<int:student_id>/', student_results, name='student-results'),
    path('results/test/<int:test_id>/', test_results, name='test-results'),
    path('results/test/<int:test_id>/average/', test_average_score, name='test-average-score'),
    path('results/test/<int:test_id>/highest/', test_highest_score, name='test-highest-score'),
]

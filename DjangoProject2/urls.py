from django.contrib import admin
from django.urls import path, include

import student_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('student_app.urls')),
]

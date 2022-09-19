"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from asyncio import create_task
from venv import create
from django import urls
from django.contrib import admin
from django.urls import path
from pytz import all_timezones
from first_app.views import *

urlpatterns = [                                         

    path('admin/', admin.site.urls),    
    path('get-stud/<int:pk>/', single_stud),
    path('get-all-stud/', all_stud),
    path('create-data/', create_data),
        

    # single api for all methods
    # path('student-api/', student_api),

    # class based view
    path('stud-class-api/', StudentAPI.as_view()),

    path("studentapi/", student_api),
    path("studentapi/<int:pk>/", student_api),

    # APIView class
    path("studentapinew/", StudentAPINew.as_view()),  # post, get--all data
    path("studentapinew/<int:pk>/", StudentAPINew.as_view()),  # post, get --all data
    
    # Mixins and GenericAPIView
    path("s-list/", StudList.as_view()),
    path("s-create/", StudCreate.as_view()),
    path("s-retrieve/<int:pk>/", StudRetrieve.as_view()),
    path("s-update/<int:pk>/", StudUpdate.as_view()),
    path("s-destory/<int:pk>/", StudDestroy.as_view()),

    # combined Mixins
    path("s-list-create/", StudListCreate.as_view()),
    path("s-retrieve-update-destroy/<int:pk>/", StudRetrieveUpdateDestroy.as_view()),


]                                     
    



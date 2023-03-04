'''School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
'''
from django.urls import path

# Basic Views
from app.views import home
from app.views import create

# Models ListViews
from app.views import RepresentativeListView
from app.views import ProfessorListView
from app.views import SubjectListView
from app.views import SectionListView
from app.views import StudentListView
from app.views import QualificationListView
from app.views import InscriptionListView

# Models DetailsViews
from app.views import RepresentativeView
from app.views import ProfessorView
from app.views import SubjectView
from app.views import SectionView
from app.views import StudentView
from app.views import QualificationView
from app.views import InscriptionView



urlpatterns = [
    path('', home, name='home'),
    path('create/<model_name>/', create, name='create'),
    
    path('representative/', RepresentativeListView.as_view(), name='representative-list'),
    path('professor/', ProfessorListView.as_view(), name='professor-list'),
    path('subject/', SubjectListView.as_view(), name='subject-list'),
    path('section/', SectionListView.as_view(), name='section-list'),
    path('student/', StudentListView.as_view(), name='student-list'),
    path('qualification/', QualificationListView.as_view(), name='qualification-list'),
    path('inscription/', InscriptionListView.as_view(), name='inscription-list'),

    path('representative/<pk>/', RepresentativeView.as_view(), name='representative-detail'),
    path('professor/<pk>/', ProfessorView.as_view(), name='professor-detail'),
    path('subject/<pk>/', SubjectView.as_view(), name='subject-detail'),
    path('section/<pk>/', SectionView.as_view(), name='section-detail'),
    path('student/<pk>/', StudentView.as_view(), name='student-detail'),
    path('qualification/<pk>/', QualificationView.as_view(), name='qualification-detail'),
    path('inscription/<pk>/', InscriptionView.as_view(), name='inscription-detail'),
    
]
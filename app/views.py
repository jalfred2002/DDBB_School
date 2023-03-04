from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from app.models import Representative
from app.models import Professor
from app.models import Subject
from app.models import Section
from app.models import Student
from app.models import Qualification
from app.models import Inscription

from app.forms import RepresentativeForm
from app.forms import ProfessorForm
from app.forms import SubjectForm
from app.forms import SectionForm
from app.forms import StudentForm
from app.forms import QualificationForm
from app.forms import InscriptionForm

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def get_form(model_name):
    form_models = {
        'representative': RepresentativeForm(),
        'professor': ProfessorForm(),
        'subject': SubjectForm(),
        'section': SectionForm(),
        'student': StudentForm(),
        'qualification': QualificationForm(),
        'inscription': InscriptionForm(),
    }
    return form_models[model_name]


def create(request, model_name):
    
    #Do backend things...
    context = {
        'title': model_name,
        'form': get_form(model_name),
    }    

    return render(request, 'app/form.html', context)

# List Views
class RepresentativeListView(ListView):
    model = Representative
    template_name = 'app/list_views/representative_list.html'


class ProfessorListView(ListView):
    model = Professor
    template_name = 'app/list_views/professor_list.html'


class SubjectListView(ListView):
    model = Subject
    template_name = 'app/list_views/subject_list.html'


class SectionListView(ListView):
    model = Section
    template_name = 'app/list_views/section_list.html'
    

class StudentListView(ListView):
    model = Student 
    template_name = 'app/list_views/student_list.html'


class QualificationListView(ListView):
    model = Qualification
    template_name = 'app/list_views/qualification_list.html'


class InscriptionListView(ListView):
    model = Inscription
    template_name = 'app/list_views/inscription_list.html'
    
    
# Detail Views
class RepresentativeView(DetailView):   
    model = Representative
    template_name = 'app/detail_views/representative_detail.html'
 
 
class ProfessorView(DetailView): 
    model = Professor
    template_name = 'app/detail_views/professor_detail.html'
    
    
class SubjectView(DetailView):
    model = Subject
    template_name = 'app/detail_views/subject_detail.html'
    
    
class SectionView(DetailView):
    model = Section
    template_name = 'app/detail_views/section_detail.html'

    
class StudentView(DetailView):
    model = Student
    template_name = 'app/detail_views/student_detail.html'
    
    
class QualificationView(DetailView):
    model = Qualification
    template_name = 'app/detail_views/qualification_detail.html'
    

class InscriptionView(DetailView):
    model = Inscription
    template_name = 'app/detail_views/inscription_detail.html'


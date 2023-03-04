from django.forms import ModelForm

from app.models import Representative
from app.models import Professor
from app.models import Subject
from app.models import Section
from app.models import Student
from app.models import Qualification
from app.models import Inscription

class RepresentativeForm(ModelForm):
    
    class Meta:
        model = Representative
        fields = ['user_id', 'document', 'phone']


class ProfessorForm(ModelForm):
    
    class Meta:
        model =  Professor
        fields = ['document','name','phone','address']


class SubjectForm(ModelForm):
    
    class Meta:
        model = Subject
        fields = ['code', 'name', 'professor_ids']
        
        
class SectionForm(ModelForm):
    
    class Meta:
        model = Section
        fields = ['subject_id', 'professor_id', 'year']
        
        
class StudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = ['representative_ids', 'section_ids', 'document', 'name', 'address', 'age', 'birth']
        
        
class QualificationForm(ModelForm):
    
    class Meta:
        model = Qualification
        fields = ['student_id', 'subject_id', 'score']
        
        
class InscriptionForm(ModelForm):
    
    class Meta:
        model = Inscription
        fields = ['student_id', 'section_id']
        
        

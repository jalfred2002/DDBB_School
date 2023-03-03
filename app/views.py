from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import authenticate
from .models import Student, Representative, Professor, Subject, Qualification
# Create your views here.

#STUDENT VIEWS
class StudentListView(ListView):
    
    model = Student
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(title="Students", **kwargs)


def get_student(request, id):
        
    student = Student.objects.get(pk=id)    
    
    if request.method == 'POST':
        print(request.POST.get('name'), request.POST.get('document'), sep='\t\t')
        user = authenticate(
            username=request.POST.get('name'),
            password=request.POST.get('document')
        )
        
        if user is not None:
            print("AUTENTICADO")
        else:
            print("NO AUTENTICADO")
            
        # student.name = request.POST.get('name')
        # student.document = request.POST.get('document')
        # student.save()
    
    return render(request, 'test.html', {'student': student})


def edit_student(request, id):
    return render(request, 'edit_student.html', {'student': Student.objects.get(pk=id)})



def get_qualification(request, id):
    students = Student.objects.filter(representative_ids=id)
    qualifications = {student.name: Qualification.objects.filter(student_id=student) for student in students}
    print(qualifications)
    return render(request, 'index.html')
    




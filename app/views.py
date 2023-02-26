from django.shortcuts import render
from django.views.generic import ListView
from .models import Student, Representative
# Create your views here.

# def test(request):
#     return render(request, 'index.html', {'name': 'Jorge'})

class StudentListView(ListView):
    
    model = Student
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Generic Title'
        print(context)
        return context
    
    
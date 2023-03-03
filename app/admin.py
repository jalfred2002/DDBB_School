from django.contrib import admin
from .models import Representative, Professor, Student, Subject, Section

# Register your models here.
@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('document', '__str__')
    # ordering = ('id',)
    # search_fields = ('name', )
    # list_display_links = ('id','name')
    # list_filter =
 

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('document', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('document', 'name')
    # ordering = ('id',)
    # search_fields = ('name', )
    # list_display_links = ('id','name')
    # list_filter = 


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # ordering = ('id',)
    # search_fields = ('name', )
    # list_display_links = ('id','name')
    # list_filter = 

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

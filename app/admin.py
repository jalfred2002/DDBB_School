from django.contrib import admin
from .models import Student, Representative

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
    search_fields = ('name', )
    list_display_links = ('id','name')
    # list_filter = 


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
    ordering = ('id',)
    # search_fields = ('name', )
    # list_display_links = ('id','name')
    # list_filter =
 



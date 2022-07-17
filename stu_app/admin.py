from pyexpat import model
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'dob', 'physics', "chemistry", "maths", "cs", "agg")
    list_filter = ('name',)
    # fields = ['name', 'dob', ('physics', 'chemistry', "maths", "cs",)]
    fieldsets = (
        ('Details', {
            'fields': ('name', 'dob',)
        }),
        ('Marks', {
            'fields': ('physics', "chemistry", "maths", "cs",)
        }),
    )
from django.contrib import admin
from .models import Course, Prof, SubChapter

# Register your models here.


class AdminSchool(admin.ModelAdmin):
    list_display = ('name', 'st_date', 'user')
    list_filter = ('prof_name', 'is_approved')
    #list_editable = ('name', 'prof_name', 'st_date')



# 'prof_name') не выводит преподавателя, говорит
# что поле не может иметь значение many to many


admin.site.register(Course, AdminSchool)
admin.site.register(Prof)
admin.site.register(SubChapter)

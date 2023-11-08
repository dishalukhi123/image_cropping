from django.contrib import admin
from .models import student 



# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


admin.site.register(student)

from django.contrib import admin
from .models import Question, User, Exam, UserQuestion

# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Exam)
admin.site.register(UserQuestion)

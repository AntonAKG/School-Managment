from django.contrib import admin

from .models import User, Grade, Student, ClassTeacher, Schedule, SubjectTeacher

admin.site.site_header = "School Management System"
admin.site.site_title = "School Management System"
admin.site.index_title = "Welcome to School Management System"
admin.site.site_url = "https://www.schoolmanagementsystem.com"

admin.site.register(User)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(ClassTeacher)
admin.site.register(Schedule)
admin.site.register(SubjectTeacher)

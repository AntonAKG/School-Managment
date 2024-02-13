import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _
from Profile.models import User


class Grade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(_("name"), max_length=5, unique=True)


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    grade = models.CharField(max_length=5)
    is_headman = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Grade, related_name='students', on_delete=models.CASCADE)


class ClassTeacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, related_name='class_teachers', on_delete=models.CASCADE)


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    grade = models.ForeignKey(Grade, related_name='schedule', on_delete=models.CASCADE)


class SubjectTeacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    subject = models.CharField(_("subject"), max_length=25)

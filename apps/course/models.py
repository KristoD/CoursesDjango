from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description should be more than 15 characters"
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "Comment can not be blank"
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    time = models.TimeField(auto_now_add=True)

    objects = CourseManager()

class Description(models.Model):
    content = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    course = models.OneToOneField(Course)

    objects = CourseManager()

class Comment(models.Model):
    content = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name = "comments")

    objects = CommentManager()


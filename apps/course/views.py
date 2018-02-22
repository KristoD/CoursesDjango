from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def index(request):
    context = {
        "courses" : Description.objects.all()
    }
    return render(request, 'course/index.html', context)

def process(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        errors = Description.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems() :
                messages.error(request, error, extra_tags=tag)
                return redirect('/')
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            Description.objects.create(content = desc, course_id = Course.objects.create(name = name).id)
            return redirect('/')

def show(request, id):
    context = {
        "id" : Description.objects.get(course_id=id).course_id,
        "name" : Description.objects.get(course_id=id).course.name,
        "desc" : Description.objects.get(course_id=id).content,
        "course_comments" : Course.objects.filter(id=id)
    }
    return render(request, 'course/show.html', context)

def comment(request, id):
    context = {
        "name" : Course.objects.get(id=id).name,
        "id" : Course.objects.get(id=id).id
    }
    return render(request, 'course/comment.html', context)

def comment_process(request):
    if request.method == "POST":
        content = request.POST['comment']
        courseid = request.POST['courseid']
        errors = Comment.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems() :
                messages.error(request, error, extra_tags=tag)
                return redirect('/comment/' + courseid + '/create')
        else:
            Course.objects.get(id=courseid).comments.create(content = content)
        return redirect('/show/' + courseid)

def destroy(request, id):
    context = {
        "id" : Description.objects.get(course_id=id).course_id,
        "name" : Description.objects.get(course_id=id).course.name,
        "desc" : Description.objects.get(course_id=id).content
    }
    return render(request, 'course/destroy.html', context)

def destroy_process(request):
    desc_id = request.POST['id']
    Description.objects.get(course_id=desc_id).course.delete()
    return redirect('/')
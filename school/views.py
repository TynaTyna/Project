from django.shortcuts import render
from .models import Course, Prof
from .forms import NameForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages


# Create your views here.


def main(request):
    return render(request, 'school/index.html',)


def all_courses(request):
    courses = Course.objects.filter(is_approved=True).order_by('name')
    prof = None
   # if 'prof_id' in request.GET:
    #    prof = Prof.objects.get(id=int(request.GET['prof_id']))
     #   courses = courses.filter(prof=prof)
    if 'search' in request.GET:
        courses = courses.filter(name__contains=request.GET['search'])
    return render(request, 'school/all_courses.html', {
        'courses': courses,
        'prof': prof
    })


def catalog(request):
    return render(request, 'school'/all_courses.html, {
        'profs': Prof.objects.filter(is_approved=True).order_by('name')
    })


def professor(request, prof):
    return render(request, 'school/all_courses.html', {
       'prof': Prof.objects.get(id=prof)
    })


def new_course(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            new_course = Course(
                name=form.cleaned_data['name'],
                st_date=form.cleaned_data['st_date'],
               # prof_name=form.cleaned_data['prof_name']
            )
            new_course.save()
            new_course.user = request.user
            new_course.save()

            messages.add_message(
                request, messages.INFO,
                'Курс {} успешно создан'.format(new_course.name)
            )

            return HttpResponseRedirect('/courses/new')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'school/new_course.html',
                  {
                        'form': form
                  })


def edit_course(request, course_id):
    if not Course.objects.filter(id=course_id).exists():
        return HttpResponseNotFound()

    course = Course.objects.get(id=course_id)
    if request.user != course.user:
        return HttpResponseNotFound()

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST, instance=course)
        # check whether it's valid:
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()

            messages.add_message(
                request, messages.INFO,
                'Курс {} успешно изменен'.format(inst.name)
            )

            return HttpResponseRedirect('/courses/new')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm(instance=course)
    return render(request, 'school/new_course.html',
                  {
                        'form': form
                  })

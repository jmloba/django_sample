from django.http import JsonResponse
from django.shortcuts import render
from .models import Course, Student
from .forms import Course_Form, Student_Form
from django.core import serializers
import json

# Create your views here.
def student_menu(request):
    context={}
    return render(request,'app_student/student_menu.html' ,context )

def student_list(request):
    courses= Course.objects.all()
    students= Student.objects.all()

    course_Form = Course_Form()
    student_Form = Student_Form()
    context={'students': students,
             'courses': courses,
             'course_Form':course_Form,
             'student_Form':student_Form
             }
    return render(request,'app_student/student_list.html' ,context )

def course_save_entry(request):
  if request.method == 'POST':
    form = Course_Form(request.POST or None)
    if form.is_valid():
      sid =  request.POST.get('h_course_uid')
      name = request.POST['name']
      if sid == '':
        s=Course(name=name)
      else:  
        print(f'data to save id : {sid}')
        s=Course(id=sid,name=name)
      s.save()  
      course_db = Course.objects.values()
      course_data = list(course_db)
      return JsonResponse({'status':'Success','course_data': course_data})
    else :
      return JsonResponse({'status':'Failed'})    
    

def course_edit(request):    
  if request.method == "POST":  
    id = request.POST.get("sid")
    course = Course.objects.get(pk=id)
    course_data = {'status':'Success','id':course.id, 'name': course.name}
    return JsonResponse(course_data)
  else:
    course_data = {'status':'Failed'}
    return JsonResponse(course_data)

def course_delete(request):    
  if request.method == "POST":  
    id = request.POST.get("sid")
    course = Course.objects.get(pk=id)
    print(f'course to  delete : {course}')
    course.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  

def student_save_entry(request):
 if request.method == 'POST':
    form = Student_Form(request.POST or None)
    if form.is_valid():
      print(f'form is valid ')
      sid =  request.POST.get('hidden-stud-id')
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      email = request.POST['email']
      mcourse= request.POST['course']
      
      print(f'course is : {mcourse}')
      course=Course.objects.get(id=mcourse)



      if sid == '':
        s=Student(firstname=firstname,
        lastname=lastname, email=email,course=course 
        )
      else:  
        print(f'data to save id : {sid}')
        s=Student(id=sid,firstname=firstname,lastname=lastname, email=email,  course=course)
      s.save()  

      print(f'data saved {s.firstname}')

      student_db = Student.objects.values('id','firstname','lastname','email','course__name')  #json
      print(f'student_db is: {student_db}')
      

 
      student_data = list(student_db)
      print(f'student_data: {student_data}')
      return JsonResponse({'status':'Success','student_data': student_data})
    else :
      print(f'invalid form')
      return JsonResponse({'status':'Failed'})    

def student_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    student = Student.objects.get(pk=id)
    print(f'course to  delete : {student}')
    student.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  
  
def student_edit(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    student = Student.objects.get(pk=id)

    student_data = {'status':'Success','id':student.id, 'firstname': student.firstname, 'lastname': student.lastname, 'email':student.email, 'course':student.course.name }
    print(f'student data :{student_data}')

    return JsonResponse(student_data )
  else:
    student_data = {'status':'Failed'}
    return JsonResponse(student_data)

from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import reverse
from .decorators import auth_user
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# ...


# from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.


def login_index1(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        password = request.POST.get('password')

        check_user = cdb.objects.filter(cname=cname, password=password)
        if check_user:
            request.session['users'] = cname
            return redirect('dashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')
    return render(request, 'login_index1.html')


@auth_user
def image_request(request):
    if request.method == 'POST':
        caption = request.POST['caption']
        image = request.FILES['image']
        upload = UploadImage(caption=caption, image=image)
        upload.save()
        return render(request, 'image-form.html', {"obj": upload, "media": upload})
    return render(request, 'image-form.html')


@auth_user
def dashboard(request):
    return render(request, 'dashboard.html')


@auth_user
def dashboardmain(request):
    return render(request, 'dashboardmain.html')


def users(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        email = request.POST['email']
        password = request.POST.get('password')
        confirm_password = request.POST['confirm_password']
        # print(uname, pwd)
        if cdb.objects.filter(cname=cname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            users = cdb(cname=cname, email=email, password=password, confirm_password=confirm_password)
            users.save()
            return redirect('login_index1')
    else:
        return render(request, 'users.html')


@auth_user
def gallery(request):
    return render(request, 'gallery.html')


@auth_user
def registration(request):
    return render(request, 'registration.html')


@auth_user
def photos(request):
    return render(request, 'photos.html')


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        n = File(name=name)
        n.save()

        obj = File.objects.all()
        return JsonResponse({"status": "Saved"})
    else:
        return JsonResponse({"status": "Not Saved"})


@auth_user
def carmodel(request):
    if request.method == 'POST':
        name = request.POST['name']
        mname = request.POST['mname']
        mn = File(name=name, mname=mname)
        mn.save()
    obj = File.objects.all()
    return render(request, 'model.html', {'name': obj})


@auth_user
def var_req(request):
    obj = File.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        mname = request.POST['mname']
        year = request.POST['year']
        varname = request.POST['varname']
        var = File(name=name, mname=mname, year=year, varname=varname)
        var.save()
    return render(request, 'varient.html', {'name': obj})


@auth_user
def todo_delete(request, id):
    obj = File.objects.get(id=id)
    obj.delete()
    return redirect('todo')


@auth_user
def logout(request):
    try:
        del request.session['users']
    except:
        return redirect('login_index1')
    return redirect('login_index1')


# def update_table():
#     if request.method == "POST":
#         name = request.POST.get("name")
#         new_value = File.objects.get(pk=id)

#         student_data = { "name": new_value.name}

#         return JsonResponse(student_data)


#         return JsonResponse({'success': True})
#     except File.DoesNotExist:
#         return JsonResponse({'success': False, 'message': 'Row does not exist.'})
# else:
#     return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def edit_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        new_value = File.objects.get(pk=id)

        student_data = {"name": new_value.name}

        return JsonResponse(student_data)


def index1(request):
    student = Student.objects.all()

    context = {
        "student": student
    }
    return render(request, 'index1.html', context)


@csrf_exempt
def save_student(request):
    if request.method == "POST":
        sid = request.POST.get("stuid")
        name = request.POST.get("name")
        email = request.POST.get("email")
        major = request.POST.get("major")

        if sid == "":
            student = Student(name=name, email=email, major=major)
        else:
            student = Student(id=sid, name=name, email=email, major=major)
        student.save()

        student_val = Student.objects.values()
        student_data = list(student_val)

        return JsonResponse({"status": "Saved", "student_data": student_data})
    else:
        return JsonResponse({"status": "Not Saved"})


@csrf_exempt
def delete_student(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        student = Student.objects.get(pk=id)
        print(student)
        student.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})


@csrf_exempt
def edit_student(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        student = Student.objects.get(pk=id)

        student_data = {"id": student.id, "name": student.name, "email": student.email, "major": student.major}

        return JsonResponse(student_data)


def todo1(request):
    obj = Category.objects.all()

    context = {
        "obj": obj
    }
    return render(request, 'todo1.html', context)


@csrf_exempt
def save_file1(request):
    if request.method == "POST":
        sid = request.POST.get("id")
        name = request.POST.get("name")

        if sid == "":
            file1 = Category(name=name)
        else:
            file1 = Category(id=sid, name=name)
        file1.save()

        file1_val = Category.objects.values()
        file1_data = list(file1_val)

        return JsonResponse({"status": "Saved", "student_data": file1_data})
    else:
        return JsonResponse({"status": "Not Saved"})


@csrf_exempt
def edit_file1(request):
    if request.method == "POST":
        id = request.POST.get("id")
        file1 = Category.objects.get(pk=id)

        file1_data = {"id": file1.id, "name": file1.name}

        return JsonResponse(file1_data)


@csrf_exempt
def delete_file1(request):
    if request.method == "POST":
        id = request.POST.get("id")
        file1 = Category.objects.get(pk=id)
        print(file1)
        file1.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})


def todo2(request):
    categories = Category.objects.all()

    context = {'categories': categories
               }
    return render(request, 'todo2.html', context)



@csrf_exempt
def save_body(request):
    if request.method == "POST":

       id = request.POST.get('id')
       bname = request.POST.get('bname')
       category_id = request.POST.get('category')


    # Check if an existing subcategory record should be updated
       if(id == ""):
           subcategory = Subcategory(bname = bname,category_id = category_id)

    # Otherwise, create a new subcategory record
       else:
          subcategory = Subcategory(id=id,bname=bname, category_id=category_id)
       subcategory.save()
       file1_val = Subcategory.objects.values()
       data = list(file1_val)
       return JsonResponse({"status": 1,'data':data})
    else:
       return JsonResponse({"status": 0})

@csrf_exempt
def edit_body(request):
    if request.method == "POST":
        id = request.POST.get("id")
        subcategory = Subcategory.objects.get(pk=id)

        data = {
            "id": subcategory.id,
            "bname": subcategory.bname,
            "category": subcategory.category.id  # changed to category id instead of object
        }

        return JsonResponse(data)


# @csrf_exempt
# def update_body(request):
#     if request.method == "POST":
#         id = request.POST.get("id")
#         bname = request.POST.get("bname")
#         category_id = request.POST.get("category")

#         subcategory = Subcategory.objects.get(pk=id)
#         subcategory.bname = bname
#         subcategory.category = Category.objects.get(pk=category_id)
#         subcategory.save()

#         return redirect('todo2')


@csrf_exempt
def delete_body(request):
    if request.method == "POST":
        id = request.POST.get("id")
        file1 = Subcategory.objects.get(pk=id)
        print(file1)
        file1.delete()

        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})


# def my_view(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'todo2.html', context)


def get_subcategories(request):
    subcategories = Subcategory.objects.all()
    data1 = {
        'subcategories': list(subcategories.values('id', 'bname', 'category__name'))
    }
    return JsonResponse(data1)


def get_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    return JsonResponse({'category_name': category.name})

# @csrf_exempt
# def save_body(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('id')
#         subcategory_names = request.POST.getlist('subcategories[]')
#         category = Category.objects.get(id=category_id)
#         for bname in subcategory_names:
#             subcategory = Subcategory(category=category, bname=bname)
#             subcategory.save()
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

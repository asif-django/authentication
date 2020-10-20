"""
xyz
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import MyUser


# Create your views here.


def user_login(request):
    """
    authenticating user
    :param request:
    :return: student detail page
    """
    if request.method == "POST":
        email = request.POST["email"]
        pasword = request.POST["password"]
        user = authenticate(request, email=email, password=pasword)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(
                reverse("user_details", args=(user.id,)))
        messages.error(request, 'Email or Password incorrect')
        return HttpResponseRedirect("/")

    return render(request, 'user/login.html')


def user_logout(request):
    """
    user get logout
    :param request:
    :return: login_page
    """
    logout(request)
    messages.success(request, 'User Logout Successfully')
    return HttpResponseRedirect('/')


def user_register(request):
    """
    user get register here
    :param request:
    :return: after successfully register it redirect to user details
    """
    if request.method == "POST":
        email = request.POST["email"]
        dob = request.POST["dob"]
        pasword = request.POST["password"]
        username = request.POST["username"]
        fathername = request.POST["father_name"]
        mothername = request.POST["mother_name"]
        nationality = request.POST["nationality"]
        photo = request.FILES["photo"]
        mobile = request.POST["mobile"]
        ssc = request.POST["ssc_marks"]
        inter = request.POST["inter_marks"]

        user_detail = MyUser.objects.create_user(email=email, password=pasword,
                                                 date_of_birth=dob,
                                                 user_name=username,
                                                 father_name=fathername,
                                                 mother_name=mothername,
                                                 nationality=nationality,
                                                 photo=photo,
                                                 mobile=mobile, ssc_marks=ssc,
                                                 inter_marks=inter)
        messages.success(request, 'User Register Successfully')
        return HttpResponseRedirect(
            reverse('user_details', args=(user_detail.id,)))

    return render(request, 'user/register.html')


def change_password(request):
    """
    user update old_password with new_password
    :param request: old_pwd and new_pwd
    :return: after update it redirect to user details
    """
    if request.method == "POST":
        old_pwd = request.POST["old_password"]
        new_pwd = request.POST["new_password"]
        cnfm_new_pwd = request.POST["cnfm_password"]
        user = MyUser.objects.get(email=request.user)
        if user.check_password(
                old_pwd) and new_pwd == cnfm_new_pwd and old_pwd != new_pwd:
            user.set_password(new_pwd)
            user.save()
            messages.success(request, 'Your Password Changed Successfully')
            return HttpResponseRedirect(
                reverse('user_details', args=(user.id,)))
        messages.error(request, 'User not Register')
        return HttpResponseRedirect("/change_pwd/")
    return render(request, 'user/change_pwd.html')


def user_details(request, stu_id=None):
    """
    get user details
    :param request: student_id
    :return:
    """
    try:
        user_dada = MyUser.objects.get(id=stu_id)
    except MyUser.DoesNotExist:
        messages.error(request, "User Does not exist")
        return HttpResponseRedirect("/")
    else:
        return render(request, 'user/user_details.html', {"data": user_dada})


def users_list(request):
    """
    get all users
    :param request:
    :return:
    """
    stu_data = MyUser.objects.all()
    return render(request, 'user/user_list.html',
                  {"data": stu_data, "id": request.user.id})

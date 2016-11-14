from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from .helpers import *

# Create your views here.


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def add_data_page(request):
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, extra=table.cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            name = create_reverse_name_add(table.tname)
            if not check_if_pk_exists(cursor, table):
                insert_data(cursor, table)
            return redirect(reverse(name), permanent=True)
    form = AccessFormInput(extra=table.cols)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(table.tname, form, list_of_data, args)
    return render(request, 'add.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def remove_data_page(request):
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, extra=table.pk)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            delete_data(cursor, table)
            name = create_reverse_name_remove(table.tname)
            return redirect(reverse(name), permanent=True)
    form = AccessFormInput(extra=table.pk)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(table.tname, form, list_of_data, args)
    return render(request, 'remove.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def edit_data_page(request):
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, extra=table.cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            table.non_pk_args = get_non_pk_args(table)
            edit_data(cursor, table)
            name = create_reverse_name_edit(table.tname)
            return redirect(reverse(name), permanent=True)
    form = AccessFormInput(extra=table.cols)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(table.tname, form, list_of_data, args)
    return render(request, 'edit.html', context)


def login_page(request):
    if request.user.is_superuser:
        return redirect(reverse('curator-home'))
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/curator/')
        return render(request, "login.html")


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def logout_view(request):
    logout(request)
    return redirect(reverse('curator-login'))


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def curator_home(request):
    context = create_context_index()
    return render(request, "index.html", context)

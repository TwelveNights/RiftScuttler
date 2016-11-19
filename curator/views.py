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
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    table.pk_labeled_cols = label_cols_with_pk(table)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=table.pk_labeled_cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            name = create_reverse_name(request, table.tname)
            error = insert_data(cursor, table)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=table.pk_labeled_cols)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(request, table, form, list_of_data, args, error)
    return render(request, 'curator/form.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def remove_data_page(request):
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=table.pk)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            name = create_reverse_name(request, table.tname)
            error = delete_data(cursor, table)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=table.pk)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(request, table, form, list_of_data, args, error)
    return render(request, 'curator/form.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def edit_data_page(request):
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    table.pk_labeled_cols = label_cols_with_pk(table)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=table.pk_labeled_cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            table.non_pk_args = get_non_pk_args(table)
            error = edit_data(cursor, table)
            name = create_reverse_name(request, table.tname)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=table.pk_labeled_cols)
    list_of_data = select_data(cursor, table.tname)
    args = get_args(table.cols)
    context = create_context(request, table, form, list_of_data, args, error)
    return render(request, 'curator/form.html', context)


def login_page(request):
    error = None
    if request.user.is_superuser:
        return redirect(reverse('curator-home'), permanent=True)
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/curator/')
            else:
                error = "The username/password is incorrect."
        return render(request, 'curator/login.html', {"error": error})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def logout_view(request):
    logout(request)
    return redirect(reverse('curator-login'))


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def curator_home(request):
    context = create_context_index()
    return render(request, 'curator/index.html', context)

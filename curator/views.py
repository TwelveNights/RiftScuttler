from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AccessFormInput
from .helpers import (insert_data, delete_data, edit_data, check_page_and_return_table, create_context_view,
                      create_context, create_reverse_name, reorder_dictionary, filter_cols_with_pk,
                      check_and_replace_none, create_context_index, parse_tables)

# Create your views here.


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def view_data_page(request):
    table = check_page_and_return_table(request)
    context = create_context_view(request, table)
    parse_tables()
    return render(request, 'curator/view-page.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def add_data_page(request):
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=table.cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            name = create_reverse_name(request, table.tname)
            error = insert_data(cursor, table)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=table.cols)
    context = create_context(request, table, form, error)
    return render(request, 'curator/form-page.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def remove_data_page(request):
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    pk = filter_cols_with_pk(table.cols)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=pk)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            name = create_reverse_name(request, table.tname)
            error = delete_data(cursor, table)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=pk)
    context = create_context(request, table, form, error)
    return render(request, 'curator/form-page.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def edit_data_page(request):
    error = None
    cursor = connection.cursor()
    table = check_page_and_return_table(request)
    if request.method == 'POST':
        form = AccessFormInput(request.POST, req=request, extra=table.cols)
        if form.is_valid():
            for (attribute, value) in form.extra_attributes():
                table.args.append([attribute, value])
            table.args = reorder_dictionary(table)
            table.args = check_and_replace_none(table)
            error = edit_data(cursor, table)
            name = create_reverse_name(request, table.tname)
            if error is None:
                return redirect(reverse(name), permanent=True)
    form = AccessFormInput(req=request, extra=table.cols)
    context = create_context(request, table, form, error)
    return render(request, 'curator/form-page.html', context)


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

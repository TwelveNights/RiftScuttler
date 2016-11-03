from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from common import utils
 
# Create your views here.
 
def index(request):
    tournament = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from tournaments")
        tournament = utils.dictfetchall(cursor)
 
    return HttpResponse(tournament)

def details(request, tournament_name, year):
    return HttpResponse("You made it to tournament!")

def series(request, tournament_name, year, id):
    return HttpResponse("You made it to series!")

def match(request, tournament_name, year, id, number):
    return HttpResponse("You made it to match!")


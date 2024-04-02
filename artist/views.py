from django.shortcuts import render

from artist.models import Artist


def register(request):
    """ artist register """


def tracks(request):



def home(request):
    """ artist dashbaoard home page """


def profile(request, slug):
    artist = Artist.objects.get(slug=slug)


    
    

def billing(request):




def submit_data_public(request):


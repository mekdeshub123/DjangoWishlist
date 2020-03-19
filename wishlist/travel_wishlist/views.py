from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

#This view will handle requests to home page

# Create your views here.
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()#create a new place from the form
        if form.is_valid():#Checks against DB constraints.
            place.save()#saves to the DB
            return redirect('place_list')#Redirect to GET view with the name place_list

    #if not a POST, or the form is not valid, render the page with the 
    # form to add a new place and list of place
    places = Place.objects.filter(visited=False).order_by('name')#it allow run query against the table and returns query set obj(s)
    new_place_form = NewPlaceForm()#form object created
    return render(request, 'travel_wishlist/wishlist.html', { 'places': places, 'new_place_form': new_place_form})

def places_visited(request):
    #Fetched the data from the database and sorted by 
    # user visited and display it in the view
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def place_was_visited(request):
    if request.method == "POST":
        pk = request.POST.get('pk')#get the pk vlaue from the form
        place = get_object_or_404(Place, pk=pk)#it tests if user rquest pk that not in the database
        place.visited = True#update the visited to true
        place.save()

        return redirect('place_list')
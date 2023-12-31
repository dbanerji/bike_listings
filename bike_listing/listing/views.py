from django.shortcuts import render,redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def index(request):
    return render(request,'listing/index.html')

def all_listings(request):
    all_listings = Listing.objects.order_by('-list_date')
    return render(request,'listing/all_listings.html',{'all_listings':all_listings})

def new_listing(request):
    if request.method !='POST':
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listing:all_listings')
    return render(request,'listing/new_listing.html',{'form':form})

def detail(request, detail_id):
    detail = Listing.objects.get(id=detail_id)
    return render(request, 'listing/detail.html', {'detail': detail})

def my_listing(request):
    my_listing = Listing.objects.order_by('-list_date')
    return render(request,'listing/my_listing.html',{'my_listing':my_listing})
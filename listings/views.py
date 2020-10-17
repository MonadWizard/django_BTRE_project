from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator


from .models import Listing
# Create your views here.

def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)  # earlyer first & see all published only

    paginator = Paginator(listings, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    paged_listing = paginator.get_page(page_number)

    context = {'listings':paged_listing}
    template_name = 'listings/listings.html'
    return render(request,template_name, context)



def listing(request, listing_id):
    # if page not available then show 404
    listing = get_object_or_404(Listing, pk=listing_id)  # (model,pk)


    context = {'listing':listing}
    template_name = 'listings/listing.html'
    return render(request,template_name, context)



def search(request):


    context = {}
    template_name = 'listings/search.html'
    return render(request,template_name, context)



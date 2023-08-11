from .models import Offers
from django.utils.safestring import mark_safe

def offers(request):
    offer = Offers.objects.all()
    offers = mark_safe(offer[0].offer_text)
    return {'off':offers}
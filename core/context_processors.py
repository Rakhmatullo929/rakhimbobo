from .models import Contact

def contact_info(request):
    try:
        contact = Contact.objects.first()
        return {'global_contact_info': contact}
    except:
        return {'global_contact_info': None} 
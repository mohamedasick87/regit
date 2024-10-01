from django.shortcuts import render,redirect
from app.models import Registration, Event
from django.http import HttpResponse
def HOME(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        # Extract individual records from the form
        name = request.POST.get('name')
        college = request.POST.get('college')
        department = request.POST.get('dept')  # Added department field
        paper_title = request.POST.get('paper_title')  # Added paper title field
        paper_submission_link = request.POST.get('paper_link')  # Added paper submission link field
        payment_link = request.POST.get('payment_link')  # Added payment submission link field
        transaction_number = request.POST.get('transaction_num')  # Added transaction number field
        whatsapp_group_link = request.POST.get('whatsapp_link')  # Added WhatsApp group link field

        technical_events = request.POST.getlist('technical_events')  # Use getlist for multiple selections
        non_technical_events = request.POST.getlist('non_technical_events')  # Use getlist for multiple selections

        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Create a new Registration instance
        registration = Registration(
            name=name,
            college=college,
            department=department,  # Set department
            paper_title=paper_title,  # Set paper title
            paper_submission_link=paper_submission_link,  # Set paper submission link
            payment_link=payment_link,  # Set payment submission link
            transaction_number=transaction_number,  # Set transaction number
            whatsapp_group_link=whatsapp_group_link,  # Set WhatsApp group link
            phone=phone,
            email=email
        )
        registration.save()  # Save the registration first

        # Add selected technical events
        for event_name in technical_events:
            event_instance, created = Event.objects.get_or_create(name=event_name, event_type='technical')
            registration.technical_events.add(event_instance)

        # Add selected non-technical events if any
        for event_name in non_technical_events:
            event_instance, created = Event.objects.get_or_create(name=event_name, event_type='non_technical')
            registration.non_technical_events.add(event_instance)

        # After saving, you can redirect to a success page or show a success message
        return HttpResponse('Registration successful!')  # Or redirect to another page

    return render(request, 'home.html')
from django.shortcuts import render , HttpResponse, redirect
from . models import  Project, Contact, Certificate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



import traceback

# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-date_completed')
    certificates = Certificate.objects.all()
    for project in projects:
        project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]

    context = {"projects": projects, "certificates": certificates}
    return render(request, 'portfolio/home.html', context)




def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not message_text:
            messages.error(request, "All fields are required.")
        else:
            try:
                validate_email(email)

                # Save to database
                Contact.objects.create(name=name, email=email, message=message_text)

                # Send email
                body = f"New Contact Form Submission\n\nName: {name}\nEmail: {email}\nMessage:\n{message_text}"
                try:
                    send_mail(
                        subject=f"Portfolio Contact From {name}",
                        message=body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[settings.RECEIVER_EMAIL],
                        fail_silently=False,
                    )
                except Exception as email_error:
                    # Log email errors but don't crash
                    print("Email sending error:", email_error)
                    traceback.print_exc()
                    messages.warning(request, "Your message was saved but email could not be sent.")

                # Success message
                messages.success(request, "Your message has been sent successfully! Thank you 😊")

                # Redirect to avoid resubmission
                return redirect('contact_view')

            except ValidationError:
                messages.error(request, "Please enter a valid email address.")
            except Exception as e:
                # Catch all other errors and log
                print("Contact form error:", e)
                traceback.print_exc()
                messages.error(request, "An error occurred while processing your message. Please try again later.")

    return render(request, "portfolio/home.html")

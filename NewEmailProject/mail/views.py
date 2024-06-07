from django.core.mail import send_mail
from .forms import talktohr_form
from django.shortcuts import render, redirect
from django.conf import settings

def talktohr(request):
    if request.method == 'POST':
        form = talktohr_form(request.POST)
        if form.is_valid():
            # Retrieve form data
            employee_id = form.cleaned_data['employee_id']
            department = form.cleaned_data['department']
            job_title = form.cleaned_data['job_title']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Prepare email content
            email_content = f"Employee ID: {employee_id}\nDepartment: {department}\nJob Title: {job_title}\nSubject: {subject}\nMessage: {message}"
            
            # Send email
            send_mail(
                subject,
                email_content,
                settings.EMAIL_HOST_USER,  # From email
                [email],  # To email (recipient)
                fail_silently=False,
            )
            
            # Redirect to success page after sending email
            return redirect('success')
    else:
        form = talktohr_form()
    return render(request, 'myapp/talktohr.html', {'form': form})

def talktohr_success(request):
    return render(request, 'myapp/talktohr_success.html')

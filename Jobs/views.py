from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def contactPage(request):
    return render(request, 'contact.html')


def servicesPage(request):
    return render(request, 'services.html')


def job_seeker_page(request):
    return render(request, 'jobseeker.html')


def employerPage(request):
    return render(request, 'employers.html')


def faqsPage(request):
    return render(request, 'faqs.html')


def errorPage(request):
    return render(request, 'error-page.html')

from django.shortcuts import render

def home_view(request):
    return render(request,"index.html")

def about_view(request):
    return render(request,"about.html")

def service_view(request):
    return render(request,"service.html")

def contact_view(request):
    return render(request,"contact.html")

def testimonial_view(request):
    return render(request,"testimonial.html")

def team_view(request):
    return render(request,"team.html")

def project_view(request):
    return render(request,"project.html")

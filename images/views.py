from django.shortcuts import render
from .models import Group,Article,Comment
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages  # new
from django.urls import reverse  # new
from .forms import ContactForm
from .bot import send_message
from .forms import CommentForm

def home_view(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request, "index.html" ,context=context)

def about_view(request):
    return render(request,"about.html")

def blog_view(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"blog.html",context)

def service_view(request):
    return render(request,"service.html")

def contact_view(request):
    
    if request.method == "GET":
        form = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]

            send_message(name,email,phone_number,description)
            form.save()
            form = ContactForm()
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...') 
            return HttpResponseRedirect(reverse('home-page'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
             
    context = {"form":form}

    return render(request, "contact.html",context)

def testimonial_view(request):
    return render(request,"testimonial.html")

def team_view(request):
    return render(request,"team.html")

def project_view(request):
    return render(request,"project.html")
def article_detail(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
          first_name = form.data.get("first_name")
          text = form.data["text"]
          rating = form.data["rating"]
          comment = Comment(
            first_name = first_name,
            text = text,
            rating = rating,
            article = article,
          )
          comment.save()
          messages.success(request,'Izoh yuborildi')
          return HttpResponseRedirect(reverse("article-detail",args=[id]))


    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id).order_by("-create_date")
    
    form = CommentForm()
    context = {"article":article,"comments":comments, "form":form}
    return render(request,"article.html",context)

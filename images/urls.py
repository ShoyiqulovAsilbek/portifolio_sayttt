from django.urls import path
from . import views
from .views import home_view,about_view,contact_view,service_view,team_view,testimonial_view,project_view,blog_view,article_detail
urlpatterns = [

path('',home_view,name = "home-page"),
path('about/',about_view,name = "about-page"),
path('service/',service_view,name = "service-page"),
path('contact/',contact_view,name = "contact-page"),
path('team/',team_view,name = "team-page"),
path('testimonial/',testimonial_view,name = "testimonial-page"),
path('project/',project_view,name = "project-page"),
path('<int:id>/',views.article_detail,name="article-detail"),
path('blog/',blog_view,  name="blog-page"),
]

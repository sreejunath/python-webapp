from django.urls import path
from . import views

urlpatterns = [
    path('',                views.home,        name='home'),
    path('about/',          views.about,       name='about'),
    path('courses/',        views.courses,     name='courses'),
    path('courses/<int:pk>/',views.course_detail, name='course_detail'),
    path('faculty/',        views.faculty,     name='faculty'),
    path('gallery/',        views.gallery,     name='gallery'),
    path('notices/',        views.notices,     name='notices'),
    path('founders/',       views.founders,    name='founders'),
    path('admission/',      views.admission,   name='admission'),
    path('admission/success/', views.admission_success, name='admission_success'),
    path('contact/',        views.contact,     name='contact'),
    path('contact/success/',views.contact_success, name='contact_success'),
]
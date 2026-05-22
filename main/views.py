from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import (
    CollegeSettings, Course, Faculty, Notice,
    GalleryCategory, GalleryImage, FounderMessage,
    AdmissionApplication, ContactMessage,
)
from .forms import AdmissionForm, ContactForm


def get_settings():
    return CollegeSettings.get()


# ── Home ──────────────────────────────────────────────────────────────────────
def home(request):
    college   = get_settings()
    courses   = Course.objects.filter(is_active=True)[:6]
    faculty   = Faculty.objects.filter(is_active=True)[:4]
    notices   = Notice.objects.filter(
                    is_active=True
                ).exclude(
                    expiry_date__lt=timezone.now().date()
                )[:5]
    gallery   = GalleryImage.objects.filter(is_active=True)[:8]
    founders  = FounderMessage.objects.filter(is_active=True)[:3]
    return render(request, 'home.html', {
        'college':  college,
        'courses':  courses,
        'faculty':  faculty,
        'notices':  notices,
        'gallery':  gallery,
        'founders': founders,
    })


# ── About ─────────────────────────────────────────────────────────────────────
def about(request):
    college  = get_settings()
    faculty  = Faculty.objects.filter(is_active=True)
    founders = FounderMessage.objects.filter(is_active=True)
    return render(request, 'about.html', {
        'college':  college,
        'faculty':  faculty,
        'founders': founders,
    })


# ── Courses ───────────────────────────────────────────────────────────────────
def courses(request):
    college = get_settings()
    courses = Course.objects.filter(is_active=True)
    return render(request, 'courses.html', {
        'college': college,
        'courses': courses,
    })


def course_detail(request, pk):
    college = get_settings()
    course  = get_object_or_404(Course, pk=pk, is_active=True)
    return render(request, 'course_detail.html', {
        'college': college,
        'course':  course,
    })


# ── Faculty ───────────────────────────────────────────────────────────────────
def faculty(request):
    college    = get_settings()
    all_faculty = Faculty.objects.filter(is_active=True)
    return render(request, 'faculty.html', {
        'college':  college,
        'faculty':  all_faculty,
    })


# ── Gallery ───────────────────────────────────────────────────────────────────
def gallery(request):
    college     = get_settings()
    categories  = GalleryCategory.objects.prefetch_related('images').all()
    all_images  = GalleryImage.objects.filter(is_active=True)
    cat_filter  = request.GET.get('cat')
    if cat_filter:
        all_images = all_images.filter(category__id=cat_filter)
    return render(request, 'gallery.html', {
        'college':    college,
        'categories': categories,
        'images':     all_images,
        'active_cat': cat_filter,
    })


# ── Notices ───────────────────────────────────────────────────────────────────
def notices(request):
    college  = get_settings()
    category = request.GET.get('category')
    notices  = Notice.objects.filter(is_active=True).exclude(
                    expiry_date__lt=timezone.now().date()
               )
    if category:
        notices = notices.filter(category=category)
    return render(request, 'notices.html', {
        'college':   college,
        'notices':   notices,
        'category':  category,
        'categories': Notice.CATEGORY_CHOICES,
    })


# ── Founders ──────────────────────────────────────────────────────────────────
def founders(request):
    college  = get_settings()
    founders = FounderMessage.objects.filter(is_active=True)
    return render(request, 'founders.html', {
        'college':  college,
        'founders': founders,
    })


# ── Admission ─────────────────────────────────────────────────────────────────
def admission(request):
    college = get_settings()
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admission_success')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {
        'college': college,
        'form':    form,
    })


def admission_success(request):
    college = get_settings()
    return render(request, 'admission_success.html', {'college': college})


# ── Contact ───────────────────────────────────────────────────────────────────
def contact(request):
    college = get_settings()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'college': college,
        'form':    form,
    })


def contact_success(request):
    college = get_settings()
    return render(request, 'contact_success.html', {'college': college})
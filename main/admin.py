from django.contrib import admin
from django.utils.html import format_html
from .models import (
    CollegeSettings, Course, Faculty, Notice,
    GalleryCategory, GalleryImage, FounderMessage,
    AdmissionApplication, ContactMessage,
)


# ── College Settings ──────────────────────────────────────────────────────────
@admin.register(CollegeSettings)
class CollegeSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('college_name', 'tagline', 'established_year',
                       'affiliation', 'accreditation')
        }),
        ('Contact', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram', 'youtube')
        }),
        ('Images', {
            'fields': ('logo', 'hero_image', 'about_image')
        }),
        ('About / Vision / Mission', {
            'fields': ('about_text', 'vision', 'mission')
        }),
    )

    def has_add_permission(self, request):
        return not CollegeSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ── Course ────────────────────────────────────────────────────────────────────
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display    = ('short_name', 'title', 'duration', 'seats', 'fee_per_year', 'is_active', 'order')
    list_editable   = ('is_active', 'order')
    list_filter     = ('is_active', 'duration')
    search_fields   = ('title', 'short_name')
    fieldsets = (
        ('Course Info', {
            'fields': ('title', 'short_name', 'description', 'image')
        }),
        ('Details', {
            'fields': ('duration', 'seats', 'fee_per_year', 'eligibility', 'highlights')
        }),
        ('Display', {
            'fields': ('is_active', 'order')
        }),
    )


# ── Faculty ───────────────────────────────────────────────────────────────────
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display    = ('photo_thumb', 'name', 'designation', 'department', 'qualification', 'is_active', 'order')
    list_editable   = ('is_active', 'order')
    list_filter     = ('designation', 'is_active')
    search_fields   = ('name', 'department', 'specialization')
    readonly_fields = ('photo_thumb',)
    fieldsets = (
        ('Personal', {
            'fields': ('name', 'photo', 'photo_thumb', 'bio')
        }),
        ('Professional', {
            'fields': ('designation', 'department', 'qualification',
                       'experience', 'specialization')
        }),
        ('Contact', {
            'fields': ('email', 'phone')
        }),
        ('Display', {
            'fields': ('is_active', 'order')
        }),
    )

    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return '—'
    photo_thumb.short_description = 'Photo'


# ── Notice ────────────────────────────────────────────────────────────────────
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display    = ('title', 'category', 'is_urgent', 'published_date', 'expiry_date', 'is_active')
    list_editable   = ('is_urgent', 'is_active')
    list_filter     = ('category', 'is_urgent', 'is_active')
    search_fields   = ('title', 'content')
    date_hierarchy  = 'published_date'
    fieldsets = (
        ('Notice', {
            'fields': ('title', 'category', 'content', 'attachment')
        }),
        ('Visibility', {
            'fields': ('is_urgent', 'is_active', 'published_date', 'expiry_date')
        }),
    )


# ── Gallery ───────────────────────────────────────────────────────────────────
@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'order')
    list_editable = ('order',)


class GalleryImageInline(admin.TabularInline):
    model  = GalleryImage
    extra  = 3
    fields = ('image', 'title', 'caption', 'order', 'is_active')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('image_thumb', 'title', 'category', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter   = ('category', 'is_active')
    search_fields = ('title', 'caption')
    readonly_fields = ('image_thumb',)

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:6px;" />', obj.image.url)
        return '—'
    image_thumb.short_description = 'Preview'


# ── Founder Messages ──────────────────────────────────────────────────────────
@admin.register(FounderMessage)
class FounderMessageAdmin(admin.ModelAdmin):
    list_display  = ('photo_thumb', 'name', 'role', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter   = ('role', 'is_active')
    search_fields = ('name',)
    readonly_fields = ('photo_thumb',)
    fieldsets = (
        ('Person', {
            'fields': ('name', 'role', 'photo', 'photo_thumb', 'signature')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Display', {
            'fields': ('is_active', 'order')
        }),
    )

    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:50%;object-fit:cover;" />', obj.photo.url)
        return '—'
    photo_thumb.short_description = 'Photo'


# ── Admission Applications ────────────────────────────────────────────────────
@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display    = ('full_name', 'course_applied', 'academic_year',
                       'gender', 'phone', 'email', 'status', 'applied_at')
    list_editable   = ('status',)
    list_filter     = ('status', 'course_applied', 'gender', 'academic_year')
    search_fields   = ('full_name', 'email', 'phone')
    date_hierarchy  = 'applied_at'
    readonly_fields = ('applied_at',)
    fieldsets = (
        ('Personal Info', {
            'fields': ('full_name', 'date_of_birth', 'gender',
                       'religion', 'category', 'nationality', 'photo')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Academic', {
            'fields': ('course_applied', 'academic_year',
                       'tenth_percent', 'twelfth_percent', 'degree_percent')
        }),
        ('Application Status', {
            'fields': ('status', 'admin_notes', 'applied_at')
        }),
    )

    def status_badge(self, obj):
        colors = {
            'pending':   '#f39c12',
            'reviewing': '#3498db',
            'accepted':  '#27ae60',
            'rejected':  '#e74c3c',
            'waitlist':  '#9b59b6',
        }
        color = colors.get(obj.status, '#999')
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 10px;'
            'border-radius:12px;font-size:12px;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'


# ── Contact Messages ──────────────────────────────────────────────────────────
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('name', 'subject', 'email', 'phone', 'is_read', 'replied', 'received_at')
    list_editable   = ('is_read', 'replied')
    list_filter     = ('is_read', 'replied')
    search_fields   = ('name', 'email', 'subject', 'message')
    date_hierarchy  = 'received_at'
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'received_at')
    fieldsets = (
        ('Message', {
            'fields': ('name', 'email', 'phone', 'subject', 'message', 'received_at')
        }),
        ('Status', {
            'fields': ('is_read', 'replied')
        }),
    )

    def has_add_permission(self, request):
        return False
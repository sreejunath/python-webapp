from django.db import models
from django.utils import timezone


# ── 1. College Settings (global info editable from admin) ────────────────────
class CollegeSettings(models.Model):
    college_name        = models.CharField(max_length=200, default="DEMO METCA")
    tagline             = models.CharField(max_length=300, blank=True)
    address             = models.TextField(blank=True)
    phone               = models.CharField(max_length=20, blank=True)
    email               = models.EmailField(blank=True)
    website             = models.URLField(blank=True)
    facebook            = models.URLField(blank=True)
    instagram           = models.URLField(blank=True)
    youtube             = models.URLField(blank=True)
    logo                = models.ImageField(upload_to='college/', blank=True, null=True)
    hero_image          = models.ImageField(upload_to='college/', blank=True, null=True)
    about_text          = models.TextField(blank=True)
    about_image         = models.ImageField(upload_to='college/', blank=True, null=True)
    established_year    = models.CharField(max_length=10, blank=True)
    affiliation         = models.CharField(max_length=300, blank=True)
    accreditation       = models.CharField(max_length=300, blank=True)
    vision              = models.TextField(blank=True)
    mission             = models.TextField(blank=True)

    class Meta:
        verbose_name        = "College Settings"
        verbose_name_plural = "College Settings"

    def __str__(self):
        return self.college_name

    def save(self, *args, **kwargs):
        # Only one settings record allowed
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ── 2. Course ─────────────────────────────────────────────────────────────────
class Course(models.Model):
    DURATION_CHOICES = [
        ('1 Year',  '1 Year'),
        ('2 Years', '2 Years'),
        ('3 Years', '3 Years'),
        ('4 Years', '4 Years'),
    ]
    title           = models.CharField(max_length=200)
    short_name      = models.CharField(max_length=50, help_text="e.g. B.Ed, M.Ed")
    description     = models.TextField()
    duration        = models.CharField(max_length=20, choices=DURATION_CHOICES, default='2 Years')
    seats           = models.PositiveIntegerField(default=50)
    eligibility     = models.TextField(help_text="Who can apply?")
    fee_per_year    = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    highlights      = models.TextField(blank=True, help_text="One highlight per line")
    image           = models.ImageField(upload_to='courses/', blank=True, null=True)
    is_active       = models.BooleanField(default=True)
    order           = models.PositiveIntegerField(default=0, help_text="Display order")
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name        = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.short_name} — {self.title}"

    def get_highlights_list(self):
        return [h.strip() for h in self.highlights.splitlines() if h.strip()]


# ── 3. Faculty ────────────────────────────────────────────────────────────────
class Faculty(models.Model):
    DESIGNATION_CHOICES = [
        ('Principal',           'Principal'),
        ('Vice Principal',      'Vice Principal'),
        ('Professor',           'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Guest Lecturer',      'Guest Lecturer'),
        ('Administrative',      'Administrative Staff'),
    ]
    name            = models.CharField(max_length=200)
    designation     = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    department      = models.CharField(max_length=200, blank=True)
    qualification   = models.CharField(max_length=300, help_text="e.g. M.Ed, Ph.D")
    experience      = models.CharField(max_length=100, blank=True, help_text="e.g. 12 years")
    specialization  = models.CharField(max_length=300, blank=True)
    bio             = models.TextField(blank=True)
    email           = models.EmailField(blank=True)
    phone           = models.CharField(max_length=20, blank=True)
    photo           = models.ImageField(upload_to='faculty/', blank=True, null=True)
    is_active       = models.BooleanField(default=True)
    order           = models.PositiveIntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['order', 'name']
        verbose_name        = "Faculty Member"
        verbose_name_plural = "Faculty"

    def __str__(self):
        return f"{self.name} — {self.designation}"


# ── 4. Notice Board ───────────────────────────────────────────────────────────
class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('general',     'General'),
        ('admission',   'Admission'),
        ('exam',        'Examination'),
        ('event',       'Event'),
        ('result',      'Result'),
        ('holiday',     'Holiday'),
        ('urgent',      'Urgent'),
    ]
    title           = models.CharField(max_length=300)
    category        = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    content         = models.TextField()
    attachment      = models.FileField(upload_to='notices/', blank=True, null=True,
                                       help_text="Optional PDF or image")
    is_urgent       = models.BooleanField(default=False, help_text="Shows a red badge")
    is_active       = models.BooleanField(default=True)
    published_date  = models.DateField(default=timezone.now)
    expiry_date     = models.DateField(blank=True, null=True, help_text="Hide after this date")
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-published_date', '-created_at']
        verbose_name        = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title

    def is_expired(self):
        if self.expiry_date:
            return timezone.now().date() > self.expiry_date
        return False


# ── 5. Gallery ────────────────────────────────────────────────────────────────
class GalleryCategory(models.Model):
    name    = models.CharField(max_length=100)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering            = ['order', 'name']
        verbose_name        = "Gallery Category"
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    category    = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='images')
    title       = models.CharField(max_length=200, blank=True)
    image       = models.ImageField(upload_to='gallery/')
    caption     = models.CharField(max_length=300, blank=True)
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['order', '-uploaded_at']
        verbose_name        = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title or f"Image {self.pk}"


# ── 6. Founder / Management Message ───────────────────────────────────────────
class FounderMessage(models.Model):
    ROLE_CHOICES = [
        ('Founder',          'Founder'),
        ('Co-Founder',       'Co-Founder'),
        ('Chairman',         'Chairman'),
        ('Vice Chairman',    'Vice Chairman'),
        ('Secretary',        'Secretary'),
        ('Principal',        'Principal'),
        ('Director',         'Director'),
        ('Managing Trustee', 'Managing Trustee'),
    ]
    name        = models.CharField(max_length=200)
    role        = models.CharField(max_length=30, choices=ROLE_CHOICES)
    message     = models.TextField()
    photo       = models.ImageField(upload_to='founders/', blank=True, null=True)
    signature   = models.ImageField(upload_to='founders/', blank=True, null=True,
                                    help_text="Optional signature image")
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['order']
        verbose_name        = "Founder / Management Message"
        verbose_name_plural = "Founder / Management Messages"

    def __str__(self):
        return f"{self.name} — {self.role}"


# ── 7. Admission Application ──────────────────────────────────────────────────
class AdmissionApplication(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('reviewing', 'Reviewing'),
        ('accepted',  'Accepted'),
        ('rejected',  'Rejected'),
        ('waitlist',  'Waitlist'),
    ]
    GENDER_CHOICES = [
        ('Male',   'Male'),
        ('Female', 'Female'),
        ('Other',  'Other'),
    ]
    # Personal info
    full_name       = models.CharField(max_length=200)
    date_of_birth   = models.DateField()
    gender          = models.CharField(max_length=10, choices=GENDER_CHOICES)
    religion        = models.CharField(max_length=100, blank=True)
    category        = models.CharField(max_length=50, blank=True,
                                       help_text="e.g. General, OBC, SC, ST")
    nationality     = models.CharField(max_length=100, default='Indian')
    # Contact
    email           = models.EmailField()
    phone           = models.CharField(max_length=20)
    address         = models.TextField()
    # Academic
    course_applied  = models.ForeignKey(Course, on_delete=models.SET_NULL,
                                        null=True, related_name='applications')
    academic_year   = models.CharField(max_length=20, help_text="e.g. 2025-26")
    tenth_percent   = models.DecimalField(max_digits=5, decimal_places=2,
                                          verbose_name="10th %")
    twelfth_percent = models.DecimalField(max_digits=5, decimal_places=2,
                                          verbose_name="12th %")
    degree_percent  = models.DecimalField(max_digits=5, decimal_places=2,
                                          verbose_name="Degree %", blank=True, null=True)
    # Documents
    photo           = models.ImageField(upload_to='admissions/photos/', blank=True, null=True)
    # Status
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes     = models.TextField(blank=True, help_text="Internal notes (not shown to applicant)")
    applied_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-applied_at']
        verbose_name        = "Admission Application"
        verbose_name_plural = "Admission Applications"

    def __str__(self):
        return f"{self.full_name} — {self.course_applied} ({self.status})"


# ── 8. Contact Message ────────────────────────────────────────────────────────
class ContactMessage(models.Model):
    name        = models.CharField(max_length=200)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20, blank=True)
    subject     = models.CharField(max_length=300)
    message     = models.TextField()
    is_read     = models.BooleanField(default=False)
    replied     = models.BooleanField(default=False)
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-received_at']
        verbose_name        = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} — {self.subject}"
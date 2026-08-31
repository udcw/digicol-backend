# create_admins.py

import os

ADMIN_CONTENT = {
    'accounts': """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
""",
    'members': """
from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'city', 'domain', 'is_active_member']
""",
    'courses': """
from django.contrib import admin
from .models import Category, Course, Enrollment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'level', 'price']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'course', 'status']
""",
    'projects': """
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
""",
    'blog': """
from django.contrib import admin
from .models import BlogCategory, Post

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_published', 'created_at']
""",
    'events': """
from django.contrib import admin
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'event_type', 'start_date']

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'event', 'is_confirmed']
""",
    'certificates': """
from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'certificate_id', 'member', 'course', 'issue_date']
""",
    'opportunities': """
from django.contrib import admin
from .models import Opportunity

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'opportunity_type', 'company', 'deadline']
""",
    'payments': """
from django.contrib import admin
from .models import Wallet, Transaction, PaymentMethod

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'wallet', 'amount', 'status']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
""",
    'community': """
from django.contrib import admin
from .models import Post, Comment, Discussion

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category']
"""
}

for app, content in ADMIN_CONTENT.items():
    with open(f'{app}/admin.py', 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f'✅ admin.py créé pour {app}')
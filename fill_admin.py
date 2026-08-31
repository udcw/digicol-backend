# fill_admin.py

import os

# Configuration des apps et leurs modèles
APPS_CONFIG = {
    'accounts': {
        'models': ['User'],
        'imports': [
            'from django.contrib.auth.admin import UserAdmin'
        ],
        'registrations': [
            'admin.site.register(User, UserAdmin)'
        ]
    },
    'members': {
        'models': ['Member'],
        'imports': [],
        'registrations': [
            '@admin.register(Member)\nclass MemberAdmin(admin.ModelAdmin):\n    list_display = ["id", "full_name", "phone", "city", "domain", "is_active_member"]\n    list_filter = ["city", "domain", "is_active_member"]\n    search_fields = ["full_name", "phone", "skills"]'
        ]
    },
    'courses': {
        'models': ['Category', 'Course', 'Enrollment'],
        'imports': [],
        'registrations': [
            '@admin.register(Category)\nclass CategoryAdmin(admin.ModelAdmin):\n    list_display = ["id", "name", "slug"]\n    prepopulated_fields = {"slug": ("name",)}',
            '@admin.register(Course)\nclass CourseAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "category", "level", "price", "is_published"]\n    list_filter = ["category", "level", "is_published"]\n    search_fields = ["title", "description"]',
            '@admin.register(Enrollment)\nclass EnrollmentAdmin(admin.ModelAdmin):\n    list_display = ["id", "member", "course", "status", "enrollment_date"]\n    list_filter = ["status"]'
        ]
    },
    'projects': {
        'models': ['Project'],
        'imports': [],
        'registrations': [
            '@admin.register(Project)\nclass ProjectAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "status", "team_size", "created_at"]\n    list_filter = ["status"]\n    search_fields = ["title", "description"]\n    filter_horizontal = ["team"]'
        ]
    },
    'blog': {
        'models': ['BlogCategory', 'Post'],
        'imports': [],
        'registrations': [
            '@admin.register(BlogCategory)\nclass BlogCategoryAdmin(admin.ModelAdmin):\n    list_display = ["id", "name", "slug"]\n    prepopulated_fields = {"slug": ("name",)}',
            '@admin.register(Post)\nclass PostAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "author", "is_published", "created_at"]\n    list_filter = ["is_published", "categories"]\n    search_fields = ["title", "content"]\n    filter_horizontal = ["categories"]'
        ]
    },
    'events': {
        'models': ['Event', 'EventRegistration'],
        'imports': [],
        'registrations': [
            '@admin.register(Event)\nclass EventAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "event_type", "start_date", "is_published"]\n    list_filter = ["event_type", "is_published", "is_free"]\n    search_fields = ["title", "description"]',
            '@admin.register(EventRegistration)\nclass EventRegistrationAdmin(admin.ModelAdmin):\n    list_display = ["id", "member", "event", "registration_date", "is_confirmed"]\n    list_filter = ["is_confirmed", "attended"]'
        ]
    },
    'certificates': {
        'models': ['Certificate'],
        'imports': [],
        'registrations': [
            '@admin.register(Certificate)\nclass CertificateAdmin(admin.ModelAdmin):\n    list_display = ["id", "certificate_id", "member", "course", "issue_date", "is_verified"]\n    list_filter = ["is_verified"]\n    search_fields = ["certificate_id", "member__full_name"]\n    readonly_fields = ["certificate_id"]'
        ]
    },
    'opportunities': {
        'models': ['Opportunity'],
        'imports': [],
        'registrations': [
            '@admin.register(Opportunity)\nclass OpportunityAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "opportunity_type", "company", "deadline", "is_published"]\n    list_filter = ["opportunity_type", "is_published", "is_remote"]\n    search_fields = ["title", "company", "description"]'
        ]
    },
    'community': {
        'models': ['Post', 'Comment', 'Discussion'],
        'imports': [],
        'registrations': [
            '@admin.register(Post)\nclass PostAdmin(admin.ModelAdmin):\n    list_display = ["id", "author", "content_preview", "likes_count", "created_at"]\n    def content_preview(self, obj):\n        return obj.content[:50] + "..."\n    content_preview.short_description = "Contenu"',
            '@admin.register(Comment)\nclass CommentAdmin(admin.ModelAdmin):\n    list_display = ["id", "author", "post", "created_at"]',
            '@admin.register(Discussion)\nclass DiscussionAdmin(admin.ModelAdmin):\n    list_display = ["id", "title", "author", "category", "is_pinned", "created_at"]'
        ]
    },
    'payments': {
        'models': ['Wallet', 'Transaction', 'PaymentMethod'],
        'imports': [],
        'registrations': [
            '@admin.register(Wallet)\nclass WalletAdmin(admin.ModelAdmin):\n    list_display = ["id", "member", "balance", "created_at"]',
            '@admin.register(Transaction)\nclass TransactionAdmin(admin.ModelAdmin):\n    list_display = ["id", "wallet", "transaction_type", "amount", "status", "created_at"]\n    list_filter = ["transaction_type", "status"]',
            '@admin.register(PaymentMethod)\nclass PaymentMethodAdmin(admin.ModelAdmin):\n    list_display = ["id", "name", "is_active", "is_sandbox"]\n    list_filter = ["is_active", "is_sandbox"]'
        ]
    }
}

def create_admin_files():
    """Crée automatiquement tous les fichiers admin.py"""
    
    for app_name, config in APPS_CONFIG.items():
        admin_path = f"{app_name}/admin.py"
        
        # Vérifier si l'app existe
        if not os.path.exists(f"{app_name}/models.py"):
            print(f"⚠️ App {app_name} n'existe pas, ignorée")
            continue
        
        # Générer le contenu
        content = []
        content.append("from django.contrib import admin")
        
        # Ajouter les imports spécifiques
        for imp in config.get('imports', []):
            content.append(imp)
        
        # Ajouter les modèles importés
        if config.get('models'):
            content.append(f"from .models import {', '.join(config['models'])}")
        
        content.append("")  # Ligne vide
        
        # Ajouter les enregistrements
        for reg in config.get('registrations', []):
            content.append(reg)
            content.append("")
        
        # Écrire le fichier
        with open(admin_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        
        print(f"✅ admin.py créé pour {app_name}")

if __name__ == '__main__':
    create_admin_files()
    print("\n🎉 Tous les fichiers admin.py ont été créés !")
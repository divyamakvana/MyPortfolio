from django.contrib import admin
from . models import Project, Contact, Certificate

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed', 'github_link')
    list_filter = ('date_completed',)
    search_fields = ('title', 'description', 'tech_stack')
admin.site.register(Certificate)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
from django.contrib import admin
from . models import Project,  Certificate

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed', 'github_link')
    list_filter = ('date_completed',)
    search_fields = ('title', 'description', 'tech_stack')
admin.site.register(Certificate)


      
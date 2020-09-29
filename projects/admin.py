from django.contrib import admin

# Register your models here.

from .models import Project

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["name","category","desc","inProgress","clientName"]
    list_editable = ["category","desc","inProgress","clientName"]

    class Meta:
        model = Project

admin.site.register(Project, ProjectModelAdmin)
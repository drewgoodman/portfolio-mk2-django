from django.contrib import admin

# Register your models here.
from .models import Skill

class SkillModelAdmin(admin.ModelAdmin):
    list_display = ["name","devicon_class","category"]
    list_editable = ["devicon_class","category"]

    class Meta:
        model = Skill

admin.site.register(Skill, SkillModelAdmin)
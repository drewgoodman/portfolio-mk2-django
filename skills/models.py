from django.db import models

# Create your models here.

SKILL_CATEGORIES = (
    ('language','Language'),
    ('framework','Framework'),
    ('tool','Tool'),
)

class Skill(models.Model):
    name = models.CharField(max_length=30)
    devicon_class = models.CharField(max_length=40, help_text="Name of skill for devicon-[skillname]-plain")
    category = models.CharField(max_length=14, choices=SKILL_CATEGORIES, default="language")

    def __str__(self):
        return self.name
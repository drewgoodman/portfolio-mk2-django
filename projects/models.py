from django.db import models

# Create your models here.

PROJECT_TYPE_CATEGORIES = (
    ('personal','PERSONAL'),
    ('draft','DRAFT'),
    ('client','CLIENT')
)

def img_upload_location(instance, filename):
    return "project/%s/%s" %(instance.id, filename)

class Project(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=14, choices=PROJECT_TYPE_CATEGORIES, default="personal")
    coverImage = models.ImageField(upload_to=img_upload_location, null=True, blank=True)
    liveURL = models.CharField(max_length=120)
    playURL = models.CharField(max_length=120)
    repoURL = models.CharField(max_length=120)
    desc = models.CharField(max_length=160)
    inProgress = models.BooleanField(default=False)
    clientName = models.CharField(max_length=80)
    clientImage = models.ImageField(upload_to=img_upload_location, null=True, blank=True)
    galleryText = models.TextField()

    def __str__(self):
        return self.name
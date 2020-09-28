
from django.shortcuts import render
from skills.models import Skill

def home_page_view(request):
    skill_cards = Skill.objects.all()
    context = {
        'skills': skill_cards
    }
    return render(request, "home.html", context)
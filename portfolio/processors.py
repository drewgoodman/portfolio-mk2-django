from django.template import RequestContext, Template

def global_context(request):
    current_year = 2020
    return {
        'current_year': current_year
    }
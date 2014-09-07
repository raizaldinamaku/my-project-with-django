from django.template.response import TemplateResponse
from mvideo.models import Video

def index(request):
    return TemplateResponse(request, "index.html", {'data': Video.objects.all() })

from django.views.generic import TemplateView

# Create your views here.


class HomeLandingView(TemplateView):
    template_name = "index.html"



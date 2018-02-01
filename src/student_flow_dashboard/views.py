from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class Dashboard(generic.TemplateView):
    template_name = "dashboard.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

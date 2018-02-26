from django.shortcuts import render
from django.views import generic
from .models import StudentFlow

# Create your views here.
class Dashboard(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		data = StudentFlow.objects.filter(category__exact="All", batch__exact="20039", year__exact="1")
		return render(request, "sankey/dashboard.html", {'data': data.values()})
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Devices
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.detail import DetailView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DevicesListView(ListView):

    model = Devices
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DevicesView(DetailView):

    model = Devices

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

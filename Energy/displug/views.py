from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Devices
from .forms import DevicesForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DevicesListView(ListView):

    model = Devices
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def schedule(request):
    form = DevicesForm()
    if request.method == 'POST':                    #if receive a POST, insert in model
        form = DevicesForm(request.POST)        #new object
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect("/displug")
    else:                                           #if is a GET, just return
        print ('Error from invalid')                #new_ap.html page
    return render(request, 'displug.html', {'form':form})
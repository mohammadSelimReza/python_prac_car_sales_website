from django.shortcuts import render, redirect
from .forms import MusicianForm
from . import models
from . import forms
from album.models import Album
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required,name='dispatch')
class create_musician(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'addmusician.html'
    success_url = reverse_lazy('homapage')
    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class update_musician(UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'addmusician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homapage')

@method_decorator(login_required,name='dispatch')
def delete_post(request, id):
    post = models.MusicianModel.objects.get(pk=id) 
    post.delete()
    # return redirect('addTask')
    return redirect('/')
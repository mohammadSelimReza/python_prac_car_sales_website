from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import CreateView
from  django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.



class create_album(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'addAlbum.html'
    success_url = reverse_lazy('homapage')
    def form_valid(self, form):
        return super().form_valid(form)
    
class update_album(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'addAlbum.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homapage')
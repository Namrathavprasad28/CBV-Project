from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from myApp.models import HOD
from django.urls import reverse_lazy
class HODListView(ListView):
    model = HOD
    #default template = hod_list.html
    #default context = hod_list

class HODDetailView(DetailView):
    model = HOD
    #default template = hod_detail.html
    #default context = hod

class HODCreateView(CreateView):
    model = HOD
    fields=("__all__")
    #default template = hod_form.html

class HODUpdateView(UpdateView):
    model = HOD
    fields=('name','sal')
    #default template = hod_form.html

class HODDeleteView(DeleteView):
    model = HOD
    success_url = reverse_lazy('hods')
    #default template = hod_confirm_delete.html

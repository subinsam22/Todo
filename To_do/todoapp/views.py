from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import Task,Links
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

import requests
from bs4 import BeautifulSoup
# Create your views here.
def add(request):
    task = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,"index.html",{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')


    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'editpage.html',{'f':f,'task':task})


class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class DetailListview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cdvdetail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    success_url = reverse_lazy('clvhome')


def web_scrap(request):
    if request.method == "POST":

        link_new=request.POST.get('page','')
        urls=requests.get(link_new)
        beautify=BeautifulSoup(urls.text,'html.parser')

        for link in beautify.find_all('a'):


            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,string_name=li_name)
        return redirect('/scraper/')
    else:

        data_value=Links.objects.all
        return render(request,'scraper.html',{'data_value':data_value})
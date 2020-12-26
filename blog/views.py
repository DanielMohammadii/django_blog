from django.shortcuts import render

from  django.views.generic import  ListView,DetailView

from  django.views.generic.edit import  CreateView,UpdateView,DeleteView

from  .models import  Post
from  django.urls import  reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"



class BlogDetailView(DetailView):
    model = Post
    template_name = "detail.html"




class BlogCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = '__all__'




class BlogUpdateView(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ['title','body']



class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')




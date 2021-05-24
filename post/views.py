from django.conf.urls import url
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView

from . import models
from .forms import PostForm

class PostListView(View):
    model=models.Post
    form_class=PostForm
    template_name='post/post_list.html'

    def get(self,request, *args, **kwargs):
        post=models.Post.objects.all()
        return render(request, self.template_name,{'object_list':post})

    def post(self,request,*args, **kwargs):
        try:
            post=models.Post.objects.get(id=request.POST.get('id'))
            post.estado='C'
            post.save()
            messages.success(request,'tarea cerrada exitosamente')
        except:
            messages.error(request,'tarea fallo al ser cerrada ')
        return redirect('/')


class PostDetailView(DetailView):

    model=models.Post

class PostCreateView(CreateView):
    model=models.Post
    form_class=PostForm
    success_url='/'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context
class PostUpdateView(UpdateView):
    model=models.Post
    form_class=PostForm
    success_url='/'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context

class PostDeleteView(DeleteView):
    model=models.Post
    success_url='/'
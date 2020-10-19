from django.views.generic import ListView, DetailView

# We are going to use a new generic class called CreateView allowing a user
# To edit,add,create & delete their blog entries

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# In order to Delete an Element, we use the Reverse_lazy imported from Django Urls
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# Within BlogCreateView we specify our database model Post, the name of our template
# post_new.html. For fields we explicitly set the database fields we want to expose
# which are title, author, and body.
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'text']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_del.html'
    success_url = reverse_lazy('home')

# We use reverse_lazy as opposed to just reverse so that it won’t execute the URL
# redirect until our view has finished deleting the blog post.
# Finally create a URL by importing our view BlogDeleteView and adding a new pattern:

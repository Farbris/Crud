# Now for the view which uses the built-in UserCreationForm and generic CreateView.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

# We’re subclassing the generic class-based view CreateView in our SignUpView class. We specify the use of the
# built-in UserCreationForm and the not-yet-created template at signup.html. And we use reverse_lazy to redirect the
# user to the log in page upon successful registration. Why use reverse_lazy here instead of reverse? The reason is
# that for all generic class based views the URLs are not loaded when the file is imported, so we have to use the
# lazy    # form of reverse to load them later when they’re available.

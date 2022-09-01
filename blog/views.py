from django.views.generic import ListView

from blog.models import Post, Tag, Category, Review


# Create your views here.
class HomePosts(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    # paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

    def get_queryset(self):
        return Post.objects.filter(draft=True)

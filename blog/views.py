from re import template
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm
from .models import Post

# Create your views here.


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]

#     return render(request, 'blog/index.html', {
#         'posts': latest_posts
#     })

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')

#     return render(request, 'blog/all-posts.html', {
#         'all_posts': all_posts
#     })

class SingePostView(View):

    def if_stored_check(self, post_id, request):
        stored_posts = request.session.get('stored_posts')
        return True if post_id in stored_posts else False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comments': post.comments.all().order_by('-id'),
            'comment_form': CommentForm(),
            'is_saved_for_later': self.if_stored_check(post.id, request)

        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # match the comment to the current post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        # if it's not valid then render the template with the already existing data and potential errors

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comments': post.comments.all().order_by('-id'),
            'comment_form': comment_form,
            'is_saved_for_later': self.if_stored_check(post.id, request)
        }
        return render(request, 'blog/post-detail.html', context)


# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     # Post.objects.get(slug=slug) # above is a shortcut instead of using try/except
#     return render(request, 'blog/post-detail.html', {
#         'post': post,
#         'post_tags': post.tags.all()
#     })

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            context['posts'] = Post.objects.filter(id__in=stored_posts)
            context['has_posts'] = True

        return render(request, 'blog/stored-post.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            # before appending check first is it's not alredy in read later/stored_post
            # post_id is from the hidden input in a form from post-detail.html
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        # override the stored session if it's either append or remove
        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')

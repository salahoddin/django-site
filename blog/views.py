from datetime import date
from django.shortcuts import render

all_posts = [
    {
        'slug': 'bike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Salahod-din',
        'date': date(2018, 7, 21),
        'title': 'Biking',
        'excerpt': "Here's an amazing view taken when we we're biking! There's nothing like the views you get when you're biking in the mountain!",
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, et? Iure sed ea voluptatem nulla id provident eum voluptatibus ipsam quam vitae eaque, pariatur nesciunt velit unde aliquid esse laboriosam?"
    },
    {
        'slug': 'learning-to-code',
        'image': 'coding.png',
        'author': 'Salahod-din',
        'date': date(2019, 7, 21),
        'title': 'Coding',
        'excerpt': "I am learning python programming language and django a python framework for web development.",
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, et? Iure sed ea voluptatem nulla id provident eum voluptatibus ipsam quam vitae eaque, pariatur nesciunt velit unde aliquid esse laboriosam?"
    },
    {
        'slug': 'hike-in-the-woods',
        'image': 'woods.jpg',
        'author': 'Salahod-din',
        'date': date(2020, 7, 21),
        'title': 'Hiking',
        'excerpt': "Viewing the nice forest from here in Mindanao!",
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, et? Iure sed ea voluptatem nulla id provident eum voluptatibus ipsam quam vitae eaque, pariatur nesciunt velit unde aliquid esse laboriosam?"
    },
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post
    })

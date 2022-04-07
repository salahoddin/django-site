from django.urls import path


from django.urls import path
from . import views

# commented this because of the changes in views.py
# urlpatterns = [
#     path('', views.starting_page, name='starting-page'),
#     path('posts', views.posts, name='posts-page'),
#     path('posts/<slug:slug>', views.post_detail, name='post-detail-page')
# ]

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.AllPostsView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.SingePostView.as_view(),
         name='post-detail-page'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later')
]

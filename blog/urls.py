from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = "blog"

# creating urls
urlpatterns = [
    path("app/", BlogListView.as_view(), name="blog_list"),
    path("<str:title>/", BlogDetailView.as_view(), name="blog_detail"),
]
# # creating urls
# urlpatterns = [
#     path('', index),
#     path("app/", blog_list, name="blog_list"),
#     path("<str:title>/", blog_detail, name="blog_detail"),
# ]

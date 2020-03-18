from django.urls import path, re_path
from .views import tweet_detail_view, tweet_list_view, TweetDetailView, TweetListView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    re_path('(?P<pk>\d+)', tweet_detail_view, name='detail'),
    #re_path('(?P<pk>\d+)', TweetDetailView.as_view(), name='detail'),
    #path('/1/', TweetDetailView.as_view(), name='detail'),
]
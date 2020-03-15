from django.urls import path
from .views import tweet_detail_view, tweet_list_view, TweetDetailView, TweetListView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    path('/1/', TweetDetailView.as_view(), name='detail'),
]
from django.urls import path
from .views import tweet_detail_view, tweet_list_view


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', tweet_list_view, name='list'),
    path('1/', tweet_detail_view, name='detail'),
]
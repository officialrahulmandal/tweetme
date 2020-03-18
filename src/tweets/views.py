from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Tweet

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get('pk')
        return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


# Create your views here.
def tweet_detail_view(request, pk=1):
    obj = Tweet.objects.get(id=pk)
    context ={
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,"tweets/list_view.html", context)
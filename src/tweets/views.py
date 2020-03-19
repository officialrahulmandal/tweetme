from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import  CreateView
from .forms import TweetModelForm
from .models import Tweet

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweets/create/"
    #queryset =Tweet.objects.all()
    #form = TweetModelForm
    #fields = ['user', 'content']
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.user = request.user
        instance.save()
        context = {
            "form" : form
        }
    return render(request, 'tweets/create_view.html', context)

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
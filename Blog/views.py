from django.shortcuts import render,get_object_or_404,redirect
from .models import Artical,Tag,Comment
from .forms import CommentForm
import mistune
from django.views.generic.list import ListView
from django.views.generic import DetailView




# Create your views here.

class IndexView(ListView):



    template_name = 'Blog/T.html'
    context_object_name = 'artical_list'

    def get_queryset(self):
        artical_list = Artical.objects.filter(status = 'P')
        for artical in artical_list:
            artical.body = mistune.markdown(artical.body, extras=['fenced-code-blocks'])

        return artical_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)

class ArticalDetail(DetailView):
    model = Artical
    template_name = 'Blog/detail.html'
    context_object_name = 'artical'
    pk_url_kwarg = 'artical_id'


    def get_object(self, queryset=None):
        obj = super(ArticalDetail, self).get_object()
        obj.views += 1
        obj.save()
        obj.body = mistune.markdown(obj.body,extras=['fenced-code-blocks'])
        return obj

    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.comment_set.all()
        kwargs['form'] = CommentForm()
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticalDetail, self).get_context_data(**kwargs)

class TagView(ListView):
    template_name = 'Blog/T.html'
    context_object_name = 'artical_list'

    def get_queryset(self):
        artical_list = Artical.objects.filter(tags = self.kwargs['tag_id'], status = 'P')
        for artical in artical_list:
            artical.body = mistune.markdown(artical.body,extras=['fenced-code-blocks'],)
        return artical_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['tag_name'] = get_object_or_404(Tag, pk = self.kwargs['tag_id'])
        return super(TagView, self).get_context_data(**kwargs)


def CommentView(request,artical_id):
    if request.method == 'POST':
        form =CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['user_name']
        body = form.cleaned_data['body']

        artical = get_object_or_404(Artical, pk=artical_id)
        new_record = Comment(user_name=name,
                                 body=body,
                                 artical=artical)
        new_record.save()
        return redirect('Blog:detail', artical_id)

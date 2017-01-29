from django.shortcuts import render
from .models import Artical,Category
import mistune
from django.views.generic.list import ListView
from django.views.generic import DetailView



def Main(request):
    return render(request,'Blog/index.html')

# Create your views here.

class IndexView(ListView):
    template_name = 'Blog/T.html'
    context_object_name = 'artical_list'

    def get_queryset(self):
        artical_list = Artical.objects.filter(status = 'P')
        for artical in artical_list:
            artical.body = mistune.markdown(artical.body,extras=['fenced-code-blocks'])
        return artical_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)

class ArticalDetail(DetailView):
    model = Artical
    template_name = 'Blog/detail.html'
    context_object_name = 'artical'
    pk_url_kwarg = 'artical_id'
    def get_object(self, queryset=None):
        obj = super(ArticalDetail, self).get_object()
        obj.body = mistune.markdown(obj.body)
        return obj

from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()
# 这是定义模板标签要用到的

@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    # context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量
    left = 3
    right = 3
    # 获取分页对象
    paginator = Paginator(object_list, page_count)
    # 从请求中获取页码号
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page) # 根据页码号获取数据页码对象
        context['current_page'] = int(page) # 将当前页码号封装进context中
        # 获取页码列表
        pages = paginator.page_range

    except PageNotAnInteger:
        object_list = paginator.page(1) # 获取首页数据页码对象
        context['current_page'] = 1
        pages = paginator.page_range

    except EmptyPage:
        # 用户传递的是一个空值，则把最后一页返回给他
        object_list = paginator.page(paginator.num_pages)
        # num_pages为总分页数
        context['currten_page'] = paginator.num_pages
        pages = paginator.page_range

    context['artical_list'] = object_list
    context['pages'] = pages  # 页码列表
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    # 用于判断是否加入省略号
    try:
        context['page_first'] = pages[0]
        context['page_last'] = pages[-1] + 1
    except IndexError:
        context['page_first'] = 1
        context['page_last'] = 2

    return ''
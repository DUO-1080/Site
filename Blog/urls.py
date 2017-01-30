from django.conf.urls import url
from Blog import views

app_name = 'Blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^detail/(?P<artical_id>\d+)/$',views.ArticalDetail.as_view(),name='detail'),
    url(r'^tags/(?P<tag_id>\d+)/$',views.TagView.as_view(),name='tag'),
    url(r'^detail/(?P<artical_id>\d+)/comment/$',views.CommentView, name='comment')

]
from django.conf.urls import url
from Blog import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^detail/(?P<artical_id>\d+)/$',views.ArticalDetail.as_view(),name='detail')

]
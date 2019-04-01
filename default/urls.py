# coding=utf-8
from django.conf.urls import url
from django.conf.urls import include
from untitled1.settings import BASE_DIR
from django.conf import settings
from django.views.static import serve
from.import views

urlpatterns = [
    url(r'^$',views.mylogin),
    url(r'^list/$', views.List),
    url(r'^login/$', views.mylogin),
    url(r'^regist/$', views.regist),
    url(r'^questionlist/$', views.questionlist),
    url(r'^toresponse/$', views.toresponse),
    url(r'^homepage/$', views.homepage),
    url(r'^selfhomepage/$', views.selfhomepage),
    #url(r'^hottopic/$', views.hottopic),
    #url(r'^comment/$', views.comment),
    url(r'^Follow/$', views.Follow),
    url(r'^answer/$', views.answerlist),
    url(r'^response/$', views.response),
    url(r'^publish/$', views.publish),
    url(r'^reply/$', views.Reply),
    url(r'^reply1/$', views.Reply1),
    url(r'^selfinfor/$', views.selfinfor),
    url(r'^hotlist/$', views.hotlist),
    url(r'^uploadimg/$',views.upload_image),
    url(r'^ckeditor', include('ckeditor_uploader.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
from django.urls import path

from . import views

app_name = 'app01'
urlpatterns = [
    path('api/hello', views.hello, name='hello'),
    path('api/article', views.article, name='article'),
    # path('api/comment/<int:pk>', views.CommentView.as_view(), name='comment'),
    path('api/comment', views.CommentView.as_view(), name='comment'),
    path('api/getcomments', views.getcomments, name='getcomments'),
    # path('api/getcomments/<int:pk>', views.getcomments, name='getcomments'),
    path('api/article/<int:pk>', views.articleinfo, name='articleinfo'),
    path('api/content/<int:pk>', views.content, name='content'),
    path('api/getarchives', views.getarchives, name='getarchives'),
    path('api/count/<int:pk>', views.CountView.as_view(), name='count'),
    path('api/opinion/<int:pk>', views.OpinionView.as_view(), name='opinion'),
    path('api/getopinion', views.getopinion, name='getopinion'),
    path('api/postopinion', views.PostOpinion.as_view(), name='postopinion'),
    # path('api/count/<int:pk>', views.count, name='count')
    # path('api/archives/<int:pk>', views.archives, name='archives'),
]
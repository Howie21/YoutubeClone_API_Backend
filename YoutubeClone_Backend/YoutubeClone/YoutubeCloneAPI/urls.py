


from django.urls import path
from . import views


urlpatterns = [
    path('comment/', views.CommentsAll.as_view() ),
    path('comment/<int:pk>/like/', views.CommentLike.as_view()),
    path("comment/<int:pk>/dislike/", views.CommentDislike.as_view()),
    path('reply/', views.ReplyAll.as_view()),

]
from django.urls import  path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


from .views import ActorViewSet,MovieViewSet,MovieActorAPIView,CommentViewSet,GETCommentAPIView,POSTCommentAPIView,DELETECommentAPIView

router=DefaultRouter()
router.register('actors',ActorViewSet)
router.register('movie',MovieViewSet)
router.register('comment',CommentViewSet,'comment')




urlpatterns=[
    path('',include(router.urls)),
    path('movies/<int:id>/actors', MovieActorAPIView.as_view()),
    path('comment/get',GETCommentAPIView.as_view()),
    path('comment/post',POSTCommentAPIView.as_view()),
    path('comment/delete/<int:id>/',DELETECommentAPIView.as_view()),
    path('api/auth/', obtain_auth_token, name='api_token_auth'),

]
# import status as status
from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from  rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from  rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Actor,Movie,Comment
from .serializers import ActorSerializers,MovieSerializers,CommentSerializers



class ActorViewSet(ReadOnlyModelViewSet):
    queryset=Actor.objects.all()
    serializer_class = ActorSerializers




class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        actors = movie.actor_m.all()
        serializer = ActorSerializers(actors, many=True)
        return Response(serializer.data)



class MovieViewSet(ReadOnlyModelViewSet):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializers
    pagination_class =LimitOffsetPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    filterset_fields=['genre']
    ordering_fields=['imdb','-imdb']
    search_fields = ["title","genre","actor_m__name"]

    @action(detail=True, methods=["GET"])
    def actor(self, request, *args, **kwargs):
        actor = self.get_object()
        serializer = ActorSerializers(actor.actor_m.all(), many=True)

        return Response(serializer.data)


    @action(detail=True,methods=["POST"])
    def add_actor(self,request,*args,**kwargs):
        movie=self.get_object()
        actor=Actor.objects.get(id=request.data.get('actor_id'))
        movie.actor_m.add(actor)
        movie.save()

        return Response(status=status.HTTP_204_NO_CONTENT)



    @action(detail=True, methods=["delete"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = Actor.objects.get(id=request.data.get('actor_id'))
        movie.actor_m.remove(actor)
        movie.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(ReadOnlyModelViewSet):
    serializer_class = CommentSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.save()


class GETCommentAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):
        comment=Comment.objects.all()
        serializer=CommentSerializers(comment,many=True)
        return Response(serializer.data)



class POSTCommentAPIView(APIView):

    def post(self,request):
        serializer=CommentSerializers(date=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class DELETECommentAPIView(APIView):

    def delete(self,request,id=None):
        comment=Comment.objects.get(id=id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





















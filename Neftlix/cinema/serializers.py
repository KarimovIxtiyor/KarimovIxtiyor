import  datetime
from django.db import models
from django.core.exceptions import ValidationError
from  rest_framework import  serializers
from rest_framework.exceptions import ValidationError

from  .models import Actor,Movie,Comment


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

    def validate_birthdate(self,value):
        value1=datetime.date(1950,1,1)
        if value<value1:
            raise ValidationError(detail="1950 dan katta yil kiriting ")

        return value



class MovieSerializers(serializers.ModelSerializer):
    actor_m=ActorSerializers(many=True)
    class Meta:
        model=Movie
        fields='__all__'



class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=("id","movie_id","text","created_date")
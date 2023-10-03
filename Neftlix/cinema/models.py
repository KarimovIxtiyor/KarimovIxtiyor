from django.db import models
from django.contrib.auth import  get_user_model

class Actor(models.Model):
    WOMEN='woman'
    MILE='mile'
    ROLES=(
        (WOMEN,'Women'),
        (MILE,'Mile')
    )

    name=models.CharField(max_length=150,blank=False,null=False)
    birthdate=models.DateField()
    gender=models.CharField(max_length=10,choices=ROLES,blank=True,null=True)

    class Meta:
        db_table='actor'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title=models.CharField(max_length=150,blank=False,null=False)
    year=models.IntegerField(blank=True,null=True)
    imdb=models.FloatField(blank=True,null=True)
    genre=models.CharField(max_length=150,blank=True,null=True)
    actor_m=models.ManyToManyField(Actor)

    view= models.PositiveIntegerField(default=0)

    class Meta:
        db_table='movie'

    def __str__(self):
        return self.title


User=get_user_model()

class Comment(models.Model):
    movie_id=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    text=models.TextField(max_length=1000)
    created_date=models.DateField()
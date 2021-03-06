from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.postgres.fields import JSONField
import datetime

class Course(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(User, through='UserCourse')
    games = models.ManyToManyField('Game', through='GameCourse')
    
class Profil(models.Model):
   user = models.OneToOneField(User)
   role = models.IntegerField()

class UserCourse(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    active = models.IntegerField(default=1)  

class Game(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=30)
    level = models.SmallIntegerField()
    text = models.TextField()
    config = JSONField(null=True, blank=True)

class GameCourse(models.Model):
    course = models.ForeignKey(Course)
    game = models.ForeignKey(Game)

class Score(models.Model):
    game = models.ForeignKey(Game)
    student = models.ForeignKey(User)
    value = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    start_time = models.TimeField(auto_now_add=True, blank=True)
    end_time = models.TimeField(null=True)
    game_data = models.TextField(null=True)

class Assignement(models.Model):
    mandatory = models.BooleanField()
    date = models.DateTimeField()
    course = models.ForeignKey(Course)
    game = models.ForeignKey(Game)

class AssignementStudent(models.Model):
    assignment = models.ForeignKey(Assignement)
    user = models.ForeignKey(User)
    score = models.ForeignKey(Score, null=True)

class GameConfig(models.Model):
    game = models.ForeignKey(Game)
    course = models.ForeignKey(Course)
    config = JSONField(null=True, blank=True)

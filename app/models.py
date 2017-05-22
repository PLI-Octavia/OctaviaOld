from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User)
    
class Profil(models.Model):
   user = models.OneToOneField(User)
   role = models.IntegerField()

class UserCourse(models.Model):
    user_id = models.ForeignKey(User)
    course_id = models.ForeignKey(Course)  

class Game(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=30)
    level = models.SmallIntegerField()
    text = models.TextField()


class GameCourse(models.Model):
    course = models.ForeignKey(Course)
    game = models.ForeignKey(Game)


class Score(models.Model):
    game = models.ForeignKey(Game)
    student = models.ForeignKey(User)
    value = models.IntegerField(null=True)
    date = models.DateTimeField()
    start_time = models.TimeField()
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



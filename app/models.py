from django.db import models

class Course(models.Model):
    anme = models.CharField(max_length=30)

class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course_id = models.ForeignKey('Course')

class Game(models.Model):
    game_name = models.CharField(max_length=255)
    game_version = models.CharField(max_length=30)
    game_level = models.SmallIntegerField()
    game_text = models.TextField()

class GameCourse(models.Model):
    course_id = models.ForeignKey('Course')
    game_id = models.ForeignKey('Games')
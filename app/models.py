from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course, null=True)


class Teacher(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course)
    salt = models.TextField(max_length=255)
    email = models.TextField(max_length=255)


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
    student = models.ForeignKey(Student)
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
    user = models.ForeignKey(Student)
    score = models.ForeignKey(Score, null=True)



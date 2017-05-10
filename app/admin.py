from django.contrib import admin
from  .models import Student
from  .models import Course
from  .models import Teacher
from  .models import Game
from  .models import GameCourse
from  .models import Score
from  .models import Assignement
from  .models import AssignementStudent



admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Game)
admin.site.register(GameCourse)
admin.site.register(Score)
admin.site.register(Assignement)
admin.site.register(AssignementStudent)

# Register your models here.

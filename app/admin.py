from django.contrib import admin
from  .models import Course
from  .models import Game
from  .models import GameCourse
from  .models import Score
from  .models import Assignement
from  .models import AssignementStudent
from  .models import Profil
from  .models import UserCourse
from  .models import GameConfig

admin.site.register(Course)
admin.site.register(Game)
admin.site.register(GameCourse)
admin.site.register(Score)
admin.site.register(Assignement)
admin.site.register(AssignementStudent)
admin.site.register(Profil)
admin.site.register(UserCourse)
admin.site.register(GameConfig)


# Register your models here.

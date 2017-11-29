from django.test import TestCase, Client
from app.models import Course, User, UserCourse, Game

class OctaviaTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Course#1")
        self.user = User.objects.create(username="root", password="secret")
        self.game = Game.objects.create(name="Game#1", version="1.2.3", level=1, text="")
        UserCourse.objects.create(user=self.user, course=self.course, active=True)
        self.c = Client()
        self.c.force_login(self.user)

    def assertResponseHas(self, body, response):
        self.assertEqual(200, response.status_code)
        self.assertIn(body, response.content)

class CourseTestCase(OctaviaTest):
    def test_see(self):
        response = self.c.get('/course/')
        self.assertResponseHas(b'Course#1', response)

class GameTestCase(OctaviaTest):
    def test_for_course(self):
        response = self.c.get(f'/course/{self.course.id}/game')
        self.assertResponseHas(b'Game#1', response)
        self.assertIn(b'/game/%d/enable' % self.game.id, response.content)
        self.assertNotIn(b'/game/%d/disable' % self.game.id, response.content)

    def test_see(self):
        response = self.c.get(f'/game/{self.game.id}')
        self.assertResponseHas(b'UnityLoader', response)

    def test_stats(self):
        response = self.c.get(f'/game/{self.game.id}/scores')
        self.assertResponseHas(b'jsDataScores = []', response)

    def test_enable_disable(self):
        course = Course.objects.create(name="Course#2")
        game = Game.objects.create(name="Game#2", version="2.3.4", level=1, text="")
        self.c.post(f'/course/{course.id}/game/{game.id}/enable')
        response = self.c.get(f'/course/{course.id}/game')
        self.assertResponseHas(b'Game#2', response)
        self.assertNotIn(b'/game/%d/enable' % game.id, response.content)
        self.assertIn(b'/game/%d/disable' % game.id, response.content)

        self.c.post(f'/course/{course.id}/game/{game.id}/disable')
        response = self.c.get(f'/course/{course.id}/game')
        self.assertResponseHas(b'Game#2', response)
        self.assertIn(b'/game/%d/enable' % game.id, response.content)
        self.assertNotIn(b'/game/%d/disable' % game.id, response.content)

class ScoreTestCase(OctaviaTest):
    def test_store(self):
        self.c.post(f'/score/{self.user.id}/{self.game.id}', {'score': 123456789})
        response = self.c.get(f'/game/{self.game.id}/scores')
        self.assertResponseHas(b'jsDataScores', response)
        self.assertNotIn(b'jsDataScores = []', response.content)
        self.assertIn(b'"value": 123456789', response.content)

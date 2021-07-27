from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Post, Topic
from ..views import topic_posts, PostListView

# boards.tests.test_view_topic_posts.TopicPostsTests.test_view_function

class TopicPostsTests(TestCase):
  def setUp(self):
    self.board = Board.objects.create(name='Django', description='Django board.')
    user = User.objects.create_user(username='john', email='john@doe.com', password='123')
    self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
    Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
    url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
    # print(url)
    self.response = self.client.get(url)

  def test_status_code(self):
    self.assertEquals(self.response.status_code, 200)

  def test_view_function(self):
    # view = resolve('/board/{}/topics/{}/'.format(self.board.pk, self.topic.pk))
    view = resolve('/board/1/topics/1/')
    # self.assertEquals(view.func, topic_posts)
    self.assertEquals(view.func.view_class, PostListView)
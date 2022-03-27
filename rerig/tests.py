from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rerig.models import Profile, Post, Review

class IndexViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no post exists, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('rerig:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts present.')
        self.assertQuerysetEqual(response.context['posts'], [])
    
class ProfileModelTests(TestCase):
    def test_create_user_profile(self):
        u = User.objects.create_user(username='test123', password='test123')
        u.save()

        self.assertEqual(len(Profile.objects.filter(user=u)), 1)
    
    def test_slug_line_creation(self):
        u = User.objects.create_user(username='Test123', password='test123')
        u.save()

        self.assertEqual(Profile.objects.filter(user=u)[0].slug, 'test123')

class PostModelTests(TestCase):
    def test_create_post_number(self):
        u = User.objects.create_user(username='Test123', password='test123')
        u.save()

        p = Post.objects.get_or_create(author=u, title='test', description='test description', category='PC')[0]
        p.author = u
        p.title = 'test'
        p.description = 'test description'
        p.category = 'PC'
        p.save()

        self.assertEqual(len(Post.objects.filter(title='test')), 1)

    def test_create_post_default_average_rating(self):
        u = User.objects.create_user(username='Test123', password='test123')
        u.save()

        p = Post.objects.get_or_create(author=u, title='test', description='test description', category='PC')[0]
        p.author = u
        p.title = 'test'
        p.description = 'test description'
        p.category = 'PC'
        p.save()

        self.assertEqual(Post.objects.filter(title='test')[0].averageRating, 0)

class ReviewModelTests(TestCase):
    def test_review_creation(self):
        u = User.objects.create_user(username='Test123', password='test123')
        u.save()

        p = Post.objects.get_or_create(author=u, title='test', description='test description', category='PC')[0]
        p.author = u
        p.title = 'test'
        p.description = 'test description'
        p.category = 'PC'
        p.save()

        r = Review.objects.get_or_create(author=u, post=p, score=2, comment='average')[0]
        r.author = u
        r.post = p
        r.score = 2
        r.comment = 'average'
        r.save()

        self.assertTrue(len(Review.objects.filter(comment='average')) > 0)

    def test_review_model_string_representation(self):
        u = User.objects.create_user(username='Test123', password='test123')
        u.save()

        p = Post.objects.get_or_create(author=u, title='test', description='test description', category='PC')[0]
        p.author = u
        p.title = 'test'
        p.description = 'test description'
        p.category = 'PC'
        p.save()

        r = Review.objects.get_or_create(author=u, post=p, score=2, comment='average')[0]
        r.author = u
        r.post = p
        r.score = 2
        r.comment = 'average'
        r.save()

        self.assertEqual(str(Review.objects.filter(comment='average')[0]), 'average')

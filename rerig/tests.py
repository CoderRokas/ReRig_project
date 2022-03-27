from django.urls import reverse
from django.contrib.auth.models import User
from rerig.models import Profile, Post, Review
from django.apps import apps
from django.test import TestCase, Client
from rerig.apps import RerigConfig

class IndexViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no post exists, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('rerig:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts present.')
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_index_view_with_post(self):
        u = User.objects.create_user(username='test123', password='test123')
        u.save()
        p = Post.objects.get_or_create(author=u, title='test', description='test description', category='PC')[0]
        response = self.client.get(reverse('rerig:index'))
        self.assertContains(response, p.title)

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.u = User.objects.create_user(username='test123')
        self.u.set_password('test123')
        self.u.save()

    def test_login_view(self):
        response = self.client.get(reverse('rerig:login'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):

        login = self.client.login(username='test123', password='test123')

        self.assertTrue(login)


class RegisterViewTests(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('rerig:search'))
        self.assertEqual(response.status_code, 200)

class AddPostViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.u = User.objects.create_user(username='test123')
        self.u.set_password('test123')
        self.u.save()
    def test_addPost_view_not_login(self):
        response = self.client.get(reverse('rerig:add_post'))
        self.assertEqual(response.status_code, 302)

    def test_addPost_view_login(self):
        login = self.client.login(username='test123', password='test123')
        self.assertTrue(login)
        response = self.client.get(reverse('rerig:add_post'))
        self.assertEqual(response.status_code, 200)

class SearchViewTests(TestCase):
    def test_search_view_basic(self):
        response = self.client.get(reverse('rerig:search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Type above to search for a post')

class AboutViewTests(TestCase):
    def test_about_view_basic(self):
        response = self.client.get(reverse('rerig:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rerig was created for people which have built their own or bought their own computer and show it off to others in the form of posts. This website was made to inspire others to create their own computer')

class ShowPostViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.u = User.objects.create_user(username='test123')
        self.u.set_password('test123')
        self.u.save()

        self.p = Post.objects.get_or_create(author=self.u, title='test', description='test description', category='PC')[0]

    def test_Post_view_exist(self):
        response = self.client.get(reverse('rerig:show_post', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('rerig/post.html')
        self.assertContains(response, self.p.title)
        self.assertContains(response, self.p.description)
        self.assertContains(response, self.p.category)
        self.assertIn('post', response.context)

    def test_Post_view_not_exist_post(self):
        response = self.client.get(reverse('rerig:show_post', args=[100]))
        self.assertEqual(response.status_code, 404)


class AppsTest(TestCase):
    def test_apps(self):
        self.assertEqual(RerigConfig.name, 'rerig')
        self.assertEqual(apps.get_app_config('rerig').name, 'rerig')



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

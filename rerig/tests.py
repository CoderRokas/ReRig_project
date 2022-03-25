from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no post exists, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('rerig:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no posts present.')
        self.assertQuerysetEqual(response.context['posts'], [])
    





# Create your tests here.

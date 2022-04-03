from django.test import TestCase, RequestFactory
from books.views import index


class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/index')
        response = index(request)
        self.assertEquals(response.status_code, 200)
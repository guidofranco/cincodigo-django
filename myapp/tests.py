from django.test import SimpleTestCase


class IndexTestCase(SimpleTestCase):

    def test_request_index(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello, world!', status_code=200)
        
from django.test import TestCase, Client


class URLTestCase(TestCase):
    def test_urls(self):
        self.url_test_helper('/')
        self.url_test_helper('/about/')
        self.url_test_helper('/team/')
        self.url_test_helper('/acknowledgements/')
        self.url_test_helper('/linguistic/')
        self.url_test_helper('/context/')
        self.url_test_helper('/arte/')
        self.url_test_helper('/sample_arte/')
        self.url_test_helper('/doctrina/')
        self.url_test_helper('/feria/')
        self.url_test_helper('/sample_doctrina/')
        self.url_test_helper('/handwritten/')
        self.url_test_helper('/sample_handwritten/')
        self.url_test_helper('/timeline/')
        self.url_test_helper('/bibliography/')
        self.url_test_helper('/arte_pdf/')
        self.url_test_helper('/outline/levanto')
        self.url_test_helper('/outline/arte')
        self.url_test_helper('/arte_original/')
        self.url_test_helper('/reg_spanish/')
        self.url_test_helper('/doctrina_pdf/')
        self.url_test_helper('/form/')
        self.url_test_helper('/resources/')
        self.url_test_helper('/index/')

    def url_test_helper(self, url, *, status_code=200):
        c = Client()
        response = c.get('/en' + url)
        self.assertEqual(response.status_code, status_code)
        response = c.get('/es' + url)
        self.assertEqual(response.status_code, status_code)

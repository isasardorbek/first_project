from django.test import TestCase, override_settings


# Create your tests here.
@override_settings(LOGIN_URL="/login/")
class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.get("/candidate/1/", follow=True)
        self.assertRedirects(response, "/login/?next=/candidate/1")
from django.test import TestCase

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _


class TestThrow(TestCase):
    def setUp(self):
        """Set up tests
        """
        self.email = "user@example.com"
        self.username = "user"
        self.password = "1234"
        user = User(email=self, username=self.username)
        user.set_password(self.password)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        self.user = user
        self.client.login(username=self.email, password=self.password)

    def populate(self):
        """Populate test with some...
        """
        # Create objects

    def testDummyView(self):
        """Dummy test
        """
        self.client.login(username=self.email, password=self.password)
        response = self.client.get(reverse("sample_dummy"))
        self.assertTemplateUsed(response, 'dummy.html')

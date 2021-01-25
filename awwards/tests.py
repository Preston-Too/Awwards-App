from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.preston = User(username = 'Preston',email = 'prestontookip@gmail.com')
        self.preston = Profile(user = self.preston,bio = 'tests',image = 'test.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.preston,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.preston.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)
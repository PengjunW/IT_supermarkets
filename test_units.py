import os
import re
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

class ProjectTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.rango_app_dir = os.path.join(self.project_base_dir, '../goods')

    def test_project_created(self):
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, ''))


        self.assertTrue(directory_exists,
                        "project configuration directory doesn't seem to exist")


class TemplateTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.template_dir = os.path.join(self.project_base_dir, 'templates')


    def test_about_template_exists(self):

        template_exists = os.path.isfile(os.path.join(self.template_dir, 'login.html'))
        self.assertTrue(template_exists,
                        "The login.html template was not found in the expected location.")


class ViewsTests(TestCase):
    def setUp(self):
        self.views_module = importlib.import_module('orders.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        name_exists = 'ShoppingCartViewset' in self.views_module_listing
        is_callable = callable(self.views_module.ShoppingCartViewset)
        self.assertTrue(name_exists, "We couldn't find the view for your ShoppingCartViewset view! ")
        self.assertTrue(is_callable, "Check you have defined your ShoppingCartViewset() view correctly. We can't execute it.")

class LoginTests(TestCase):
    def test_login_url_exists(self):
        """
        Checks to see if the new login view exists in the correct place, with the correct name.
        """
        url = ''

        try:
            url = reverse('users:login')
        except:
            pass

        self.assertEqual(url, '/users/login/',
                         "Have you created the user:login URL mapping correctly?")
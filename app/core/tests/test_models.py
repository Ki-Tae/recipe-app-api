from django.test import TestCase
from django.contrib.auth import get_user_model
# importing user directly is not recommended in django
# instead use get_user_model function to import user

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test email for a new user is normalized"""
        email = "test@EXAMPLE.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            # code below here should raise Value Error
            #  or else the test will fail
            get_user_model().objects.create_user(None, 'test123')
    
    def test_create_new_super_user(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            '123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
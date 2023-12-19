from django.test import TestCase
from coffe.models import CustomUserManager, MyUser, Category


class TestMyUser(TestCase):
    def test_create_user(self):
        user = MyUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            role='A',
            phone='1234567890',
            gender='F',
            address='Test Address'
        )
        self.assertIsNotNone(user)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_customer)

    def test_create_superuser(self):
        superuser = MyUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='A',  # Add the role as per your model definition
            phone='1234567890',  # Add other required fields
            gender='M',
            address='Admin Address'
        )

        self.assertIsNotNone(superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_string_representation(self):
        user = MyUser(username="user name", password='password')
        self.assertEqual(str(user), user.username)

    def test_manager_usage(self):
        user = MyUser.objects.create_user(username="user name", password='password', email='test@email.com')
        self.assertIsNotNone(user)

    def test_default_value(self):
        user = MyUser.objects.create_user(username="user name", password='password', email='test@email.com')
        self.assertTrue(user.is_customer)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_manager)
        self.assertFalse(user.is_superuser)

    def test_unique_instances(self):
        user1 = MyUser.objects.create_user(username="user name", password='password1', email='test1@email.com')
        with self.assertRaises(Exception):
            user2 = MyUser.objects.create_user(username="user name", password='password2', email='test2@email.com')


class TestCategoryModel(TestCase):
    def setUp(self):
        Category.objects.create(name='cat1')
        Category.objects.create(name='cat2')
        Category.objects.create(name='cat3')

    def test_category_creation(self):
        category_count = Category.objects.count()
        self.assertEquals(category_count, 3)












# class TestCustomUserManager(TestCase):
#     def test_create_user(self):
#         manager = CustomUserManager()
#         user = manager.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='password123',
#             role='A',  # Add the role as per your model definition
#             phone='1234567890',  # Add other required fields
#             gender='F',
#             address='Test Address'
#         )
#
#         self.assertIsNotNone(user)
#         self.assertFalse(user.is_staff)
#         self.assertTrue(user.is_customer)
#
#
#     def test_create_superuser(self):
#         manager = CustomUserManager()
#         superuser = manager.create_superuser(
#             username='admin',
#             email='admin@example.com',
#             password='admin123',
#             role='A',
#             phone='1234567890',
#             gender='M',
#             address='Admin Address'
#         )
#
#         self.assertIsNotNone(superuser)
#         self.assertTrue(superuser.is_staff)
#         self.assertTrue(superuser.is_superuser)
#
#
#
#     def test_create_superuser_with_invalid_flags(self):
#         manager = CustomUserManager()
#         with self.assertRaises(ValueError):
#             manager.create_superuser(
#                 username='admin',
#                 email='admin@example.com',
#                 password='admin123',
#                 role='A',
#                 phone='1234567890',
#                 gender='M',
#                 address='Admin Address',
#                 is_staff=False
#             )
#
#         with self.assertRaises(ValueError):
#             manager.create_superuser(
#                 username='admin',
#                 email='admin@example.com',
#                 password='admin123',
#                 role='A',
#                 phone='1234567890',
#                 gender='M',
#                 address='Admin Address',
#                 is_superuser=False
#             )

from django.http import HttpRequest
from django.test import TestCase
from coffe.forms import CustomerCreationModelForm
from coffe.models import MyUser


class CustomerCreationModleFormTest(TestCase):
    def test_form_has_fields(self):
        form = CustomerCreationModelForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('gender', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('phone', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        self.assertIn('address', form.fields)

    def test_form_has_no_fields(self):
        form = CustomerCreationModelForm()
        self.assertNotIn('roles', form.fields)
        self.assertNotIn('age', form.fields)
        self.assertNotIn('date_of_birth', form.fields)
        self.assertNotIn('date_joined', form.fields)
        self.assertNotIn('is_active', form.fields)
        self.assertNotIn('is_staff', form.fields)
        self.assertNotIn('is_superuser', form.fields)
        self.assertNotIn('is_manager', form.fields)

    def test_valid_form(self):
        """all field must be fill with true data"""
        form_data = {
            "first_name": "Iman",
            "last_name": "Gholami",
            "gender": "M",
            "email": 'iman@email.com',
            "phone": '01234567',
            "username": 'iman',
            "password": 'iman@123',
            "address": 'Parand',
        }
        form = CustomerCreationModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "first_name": "Iman",
            "last_name": "Gholami",
            "gender": "M",
            "email": 'iman@email.com',
            "phone": '',
            "username": 'iman',
            "password": 'iman@123',
            "address": 'Parand',
        }
        form = CustomerCreationModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_gender_choice(self):
        form = CustomerCreationModelForm()
        gender_choices = form.fields['gender'].choices
        self.assertEquals(gender_choices, [("", "---------"), ("F", "Female"), ("M", "Male"), ("o", "other"), ])

    def test_unique_field(self):
        """ username field must be unique"""
        user = MyUser.objects.create_user(username='iman')
        form_data = {
            "first_name": "Iman",
            "last_name": "Gholami",
            "gender": "M",
            "email": 'iman@email.com',
            "phone": '+12345678',
            "username": 'iman',
            "password": 'iman@123',
            "address": 'Parand',
        }
        form = CustomerCreationModelForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_password_validation(self):
        """ test password validation rules"""
        form_data = {
            "first_name": "Iman",
            "last_name": "Gholami",
            "gender": "M",
            "email": 'iman@email.com',
            "phone": '+12345678',
            "username": 'iman',
            "password": '',
            "address": 'Parand',
        }
        form = CustomerCreationModelForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_form_save(self):
        """check save method"""
        form_data = {
            "first_name": "Iman",
            "last_name": "Gholami",
            "gender": "M",
            "email": 'iman@email.com',
            "phone": '01234567',
            "username": 'iman',
            "password": 'iman@123',
            "address": 'Parand',
        }
        form = CustomerCreationModelForm(data=form_data)
        self.assertTrue(form.is_valid())
        new_user = form.save()
        self.assertIsInstance(new_user, MyUser)

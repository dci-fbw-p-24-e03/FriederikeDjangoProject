import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import CustomUserProfile


# Models Testing
class CustomUserProfileTests(TestCase):
    """Test the CustomUserProfile model"""

    def setUp(self):
        self.invalid_user = CustomUserProfile.objects.create_user(
            username="invalid_testuser",
            password="invalidtestusers_password",
            email="ivalid_tesuser@testemail.com",
            first_name="Invalid",
            last_name="User",
            date_of_birth=timezone.now().date(),
            profession="MA",
            phone_number="+49 345 123456789",
            sex="F",
            sold_items_count=3,
        )

        self.valid_user = CustomUserProfile.objects.create_user(
            username="valid_testuser",
            password="validtestusers_password",
            email="valid_tesuser@testemail.com",
            first_name="Valid",
            last_name="User",
            date_of_birth="1988-12-02",
            profession="MA",
            phone_number="+49 345 123456789",
            sex="F",
            sold_items_count=3,
        )

    def test_user_creation(self):
        self.assertEqual(CustomUserProfile.objects.count(), 2)
        self.assertEqual(self.invalid_user.first_name, "Invalid")
        self.assertEqual(self.valid_user.first_name, "Valid")
        self.assertEqual(self.valid_user.sold_items_count, 3)

    def test_validate_user_age(self):
        with self.assertRaises(ValidationError):
            self.invalid_user.full_clean()

    def test_phone_validator(self):
        try:
            self.valid_user.full_clean()
        except ValidationError:
            self.fail("test_phone_validator raised ValidationError")

    def test_increment_sold_items(self):
        self.valid_user.increment_sold_items()
        self.assertEqual(self.valid_user.sold_items_count, 4)


# Views Testing
class UserLoginViewTest(TestCase):
    def setUp(self):
        self.valid_user = CustomUserProfile.objects.create_user(
            username="valid_testuser",
            password="validtestusers_password",
            email="valid_tesuser@testemail.com",
            first_name="Valid",
            last_name="User",
            date_of_birth="1988-12-02",
            profession="MA",
            phone_number="+49 345 123456789",
            sex="F",
            sold_items_count=3,
        )
        self.valid_user_login = {
            "username": "valid_testuser",
            "password": "validtestusers_password",
        }

    def test_login(self):
        response = self.client.post(
            "accounts/login.html", self.valid_user_login, follow=True
        )
        print(response.context)
        self.assertTrue(response.context["user"].is_active())

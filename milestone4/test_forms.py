from django.test import TestCase

# Create your tests here.


class TestRegisterSellerForm(TestCase):
    def test_seller_username_is_required():
        form = SellerForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['username'])

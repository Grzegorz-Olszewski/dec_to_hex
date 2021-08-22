from django.test import TestCase
from django.urls import reverse


class TestDecToHex(TestCase):
    def test_zero(self):
        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '0'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'0')

    def test_string(self):
        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': 'three'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b"Number has to be an integer")

    def test_float(self):
        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '1.543'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b"Number has to be an integer")

    def test_negative(self):
        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '-12232'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'-2FC8')

    def test_correct_positive_numbers(self):
        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '12232'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'2FC8')

        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '10'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'A')

        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '15'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'F')

        response = self.client.post(
            reverse('decimal_to_hex'),
            {'number': '4'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'4')

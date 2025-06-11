from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Wallet
import uuid


class WalletAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.wallet = Wallet.objects.create(balance=100)
        self.wallet_url = f"/api/v1/wallets/{self.wallet.id}"
        self.operation_url = f"/api/v1/wallets/{self.wallet.id}/operation"

    def test_get_wallet_balance(self):
        response = self.client.get(self.wallet_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.data["balance"]), 100)

    def test_deposit(self):
        data = {"operation_type": "DEPOSIT", "amount": 50}
        response = self.client.post(self.operation_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(int(self.wallet.balance), 150)

    def test_withdraw(self):
        data = {"operation_type": "WITHDRAW", "amount": 30}
        response = self.client.post(self.operation_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(int(self.wallet.balance), 70)

    def test_invalid_operation_type(self):
        data = {"operation_type": "TRANSFER", "amount": 10}
        response = self.client.post(self.operation_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("operation_type", str(response.data))

    def test_wallet_not_found(self):
        random_uuid = uuid.uuid4()
        url = f"/api/v1/wallets/{random_uuid}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

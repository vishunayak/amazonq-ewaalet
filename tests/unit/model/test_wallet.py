import unittest
import sys
sys.path.append('.')

import boto3
from ewallet.model.wallet import Wallet
from ewallet.model.transaction import TransactionType, TransactionStatus

class WalletTest(unittest.TestCase):

  def test_wallet_creation(self):
    wallet = Wallet('test_wallet')
    self.assertDictEqual(wallet.balance, {})
    self.assertCountEqual(wallet.transactions, [])
    self.assertEqual(wallet.id, None)
    self.assertEqual(wallet.name, 'test_wallet')

  def test_list_balance(self):
    wallet = Wallet('test_wallet')
    wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
    wallet.add_transaction(300, 'EUR', TransactionType.TOP_UP)
    wallet.add_transaction(50, 'GBP', TransactionType.TOP_UP)
    wallet.withdraw(50, 'GBP')

    balance = wallet.list_balance()

    self.assertListEqual(balance, ['USD 100.00', 'EUR 300.00', 'GBP 0.00'])

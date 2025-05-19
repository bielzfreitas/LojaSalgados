import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Salgados de Festa', response.data)

    def test_order_salgado(self):
        response = self.app.post('/order', data={'salgado': 'coxinha', 'quantity': 10})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pedido recebido', response.data)

if __name__ == '__main__':
    unittest.main()
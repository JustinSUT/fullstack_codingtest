import unittest
from app import create_app

class ProductApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_add_product(self):
        response = self.client.post("/api/products/", json={
            "name": "Product 1",
            "price": 10.99
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_get_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        # First add a product
        self.client.post("/api/products/", json={"name": "Product 1", "price": 10.99})
        response = self.client.put("/api/products/1", json={"price": 12.99})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["price"], 12.99)

    def test_delete_product(self):
        self.client.post("/api/products/", json={"name": "Product 1", "price": 10.99})
        response = self.client.delete("/api/products/1")
        self.assertEqual(response.status_code, 200)

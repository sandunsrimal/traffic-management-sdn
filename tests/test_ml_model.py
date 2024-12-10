import unittest
import joblib

class TestMLModel(unittest.TestCase):
    def test_model_exists(self):
        model = joblib.load("ml_model/models/load_balancer.pkl")
        self.assertIsNotNone(model, "ML model is not initialized!")

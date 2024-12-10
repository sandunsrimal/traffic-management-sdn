import unittest
from rl_agent.rl_main import model

class TestRLAgent(unittest.TestCase):
    def test_model_exists(self):
        self.assertIsNotNone(model, "RL model is not initialized!")

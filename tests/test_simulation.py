# tests/test_simulation.py

import unittest
from busy_beaver.simulation import simulate_machine

class TestSimulation(unittest.TestCase):
    def test_simulate_halt(self):
        transition_dict = {
            ("A", 0): (1, "R", "H"),
            ("A", 1): (1, "L", "H"),
            ("B", 0): (0, "R", "H"),
            ("B", 1): (0, "L", "H"),
            ("C", 0): (0, "R", "H"),
            ("C", 1): (0, "L", "H"),
        }
        result = simulate_machine(transition_dict, max_steps=10)
        self.assertIsNotNone(result)
        ones, steps, _ = result
        self.assertEqual(ones, 1)
        self.assertEqual(steps, 1)

    def test_simulate_non_halt(self):
        transition_dict = {
            ("A", 0): (0, "R", "A"),
            ("A", 1): (1, "L", "A"),
            ("B", 0): (0, "R", "A"),
            ("B", 1): (1, "L", "A"),
            ("C", 0): (0, "R", "A"),
            ("C", 1): (1, "L", "A"),
        }
        result = simulate_machine(transition_dict, max_steps=5)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

# tests/test_turing_machine.py

import unittest
from busy_beaver.turing_machine import TuringMachine


class TestTuringMachine(unittest.TestCase):
    def test_halt_immediately(self):
        transition_function = {}
        tm = TuringMachine(transition_function, start_state="A", halt_states=["A"])
        halted, ones, steps = tm.run()
        self.assertTrue(halted)
        self.assertEqual(ones, 0)
        self.assertEqual(steps, 0)

    def test_single_step(self):
        transition_function = {("A", 0): (1, "R", "H")}
        tm = TuringMachine(transition_function, start_state="A", halt_states=["H"])
        halted, ones, steps = tm.run()
        self.assertTrue(halted)
        self.assertEqual(ones, 1)
        self.assertEqual(steps, 1)

    def test_non_halt(self):
        transition_function = {("A", 0): (0, "R", "A")}
        tm = TuringMachine(
            transition_function, start_state="A", halt_states=["H"], max_steps=10
        )
        halted, ones, steps = tm.run()
        self.assertFalse(halted)
        self.assertEqual(ones, 0)
        self.assertEqual(steps, 10)


if __name__ == "__main__":
    unittest.main()

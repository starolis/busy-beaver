# busy_beaver/turing_machine.py


class TuringMachine:

    def __init__(self,
                 transition_function,
                 start_state,
                 halt_states,
                 max_steps=10000):
        self.transition_function = transition_function
        self.current_state = start_state
        self.halt_states = halt_states
        self.tape = {}
        self.head = 0
        self.step_count = 0
        self.max_steps = max_steps

    def step(self):
        symbol = self.tape.get(self.head, 0)
        if (self.current_state, symbol) in self.transition_function:
            write, move, next_state = self.transition_function[(
                self.current_state, symbol)]
            self.tape[self.head] = write
            if move == "R":
                self.head += 1
            elif move == "L":
                self.head -= 1
            self.current_state = next_state
            self.step_count += 1
            return True  # Continue
        else:
            return False  # Halt

    def run(self):
        while self.step_count < self.max_steps:
            if self.current_state in self.halt_states:
                # Machine has halted
                ones_count = sum(1 for v in self.tape.values() if v == 1)
                return (True, ones_count, self.step_count)
            if not self.step():
                # Machine has halted due to no transition defined
                ones_count = sum(1 for v in self.tape.values() if v == 1)
                return (True, ones_count, self.step_count)
        # Machine did not halt within max_steps
        return (False, 0, self.step_count)

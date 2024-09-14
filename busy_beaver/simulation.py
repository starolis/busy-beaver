# busy_beaver/simulation.py

import itertools
import multiprocessing
from functools import partial
from .turing_machine import TuringMachine

# Define the Turing machine components
states = ["A", "B", "C"]
halt_state = "H"
symbols = [0, 1]
directions = ["L", "R"]

def simulate_machine(
    transition_function, start_state="A", halt_states=[halt_state], max_steps=100
):
    tm = TuringMachine(
        transition_function=transition_function,
        start_state=start_state,
        halt_states=halt_states,
        max_steps=max_steps,
    )
    halted, ones, steps = tm.run()
    if halted:
        return (ones, steps, transition_function)
    else:
        return None  # Indicates non-halting machine

def worker_simulate(tf):
    # Build the transition dictionary
    transition_dict = {}
    for i, state in enumerate(states):
        for j, symbol in enumerate(symbols):
            action = tf[i * len(symbols) + j]
            transition_dict[(state, symbol)] = action
    # Simulate the machine
    result = simulate_machine(
        transition_function=transition_dict,
        start_state="A",
        halt_states=[halt_state],
        max_steps=10000,
    )
    return result  # Either (ones, steps, transition_dict) or None

def main():
    # Possible next states include all states plus the halt state
    all_states = states + [halt_state]

    # Generate all possible transition actions
    # Each action is a tuple: (write_symbol, move_direction, next_state)
    transition_actions = list(itertools.product(symbols, directions, all_states))

    # Calculate the number of possible actions per transition
    actions_per_transition = (
        len(symbols) * len(directions) * len(all_states)
    )  # 2 * 2 * 4 = 16

    # Calculate the number of transitions per machine
    transitions_per_machine = len(states) * len(symbols)  # 3 * 2 = 6

    # Calculate the total number of machines
    total_machines = actions_per_transition**transitions_per_machine  # 16^6 = 16777216

    # Enumerate all possible transition functions
    all_transition_functions = itertools.product(
        transition_actions, repeat=transitions_per_machine
    )

    # Initialize tracking variables
    max_ones_found = 0
    best_productivity_machine = None

    max_steps_found = 0
    best_step_machine = None

    halted_machines = 0
    non_halted_machines = 0

    machine_count = 0

    # Set up multiprocessing pool
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)

    try:
        # Use imap_unordered for better performance
        for result in pool.imap_unordered(worker_simulate, all_transition_functions):
            machine_count += 1
            if result is not None:
                ones, steps, transition_dict = result
                halted_machines += 1
                # Check for Productivity Busy Beaver
                if ones > max_ones_found:
                    max_ones_found = ones
                    best_productivity_machine = transition_dict
                # Check for Longest Halting Busy Beaver
                if steps > max_steps_found:
                    max_steps_found = steps
                    best_step_machine = transition_dict
            else:
                non_halted_machines += 1
            # Progress reporting
            if machine_count % 1000 == 0 or machine_count == total_machines:
                print(
                    f"Processed {machine_count} machines out of {total_machines}. "
                    f"Current max 1's: {max_ones_found}, "
                    f"Current max steps: {max_steps_found}"
                )
    finally:
        pool.close()
        pool.join()

    # After all machines are processed, print the results
    print(f"\nTotal Machines Processed: {machine_count}")
    print(f"Halting Machines: {halted_machines}")
    print(f"Non-Halting Machines (Hit Step Limit): {non_halted_machines}\n")

    if best_productivity_machine:
        print(
            f"Productivity Busy Beaver for n=3 produces {max_ones_found} 1's on the tape."
        )
        print("Best Productivity Machine Transitions:")
        for key, value in best_productivity_machine.items():
            print(
                f"State {key[0]}, Read {key[1]}: Write {value[0]}, Move {value[1]}, Next {value[2]}"
            )
    else:
        print(
            "No halting machines found within the step limit for Productivity Busy Beaver."
        )

    if best_step_machine:
        print(
            f"\nLongest Halting Busy Beaver for n=3 completes {max_steps_found} steps."
        )
        print("Best Longest Halting Machine Transitions:")
        for key, value in best_step_machine.items():
            print(
                f"State {key[0]}, Read {key[1]}: Write {value[0]}, Move {value[1]}, Next {value[2]}"
            )
    else:
        print(
            "\nNo halting machines found within the step limit for Longest Halting Busy Beaver."
        )

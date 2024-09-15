import itertools
import asyncio
from functools import partial
from .turing_machine import TuringMachine

# Define the Turing machine components
symbols = [0, 1]
directions = ["L", "R"]

# Global queue for progress updates
progress_queue = asyncio.Queue()

async def send_progress_update(progress):
    await progress_queue.put(progress)

def simulate_machine(
    transition_function, start_state="A", halt_states=["H"], max_steps=100000
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

async def worker_simulate(tf):
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
        halt_states=["H"],
        max_steps=max_steps,
    )
    return result  # Either (ones, steps, transition_dict) or None

async def run_simulation(num_states, max_steps):
    global states, max_steps
    states = [chr(65 + i) for i in range(num_states)]  # Generate states A, B, C, ...
    max_steps = max_steps

    # Possible next states include all states plus the halt state
    all_states = states + ["H"]

    # Generate all possible transition actions
    transition_actions = list(itertools.product(symbols, directions, all_states))

    # Calculate the total number of machines
    total_machines = len(transition_actions) ** (len(states) * len(symbols))

    # Initialize tracking variables
    max_ones_found = 0
    best_productivity_machine = None
    max_steps_found = 0
    best_step_machine = None
    halted_machines = 0
    non_halted_machines = 0
    machine_count = 0

    # Generate all possible transition functions
    all_transition_functions = itertools.product(
        transition_actions, repeat=len(states) * len(symbols)
    )

    for tf in all_transition_functions:
        result = await worker_simulate(tf)
        machine_count += 1
        if result is not None:
            ones, steps, transition_dict = result
            halted_machines += 1
            if ones > max_ones_found:
                max_ones_found = ones
                best_productivity_machine = transition_dict
            if steps > max_steps_found:
                max_steps_found = steps
                best_step_machine = transition_dict
        else:
            non_halted_machines += 1

        # Send progress update
        progress = (machine_count / total_machines) * 100
        await send_progress_update(progress)

        # Optional: yield control to allow other coroutines to run
        if machine_count % 1000 == 0:
            await asyncio.sleep(0)

    results = {
        "max_ones": max_ones_found,
        "max_steps": max_steps_found,
        "best_productivity_machine": best_productivity_machine,
        "best_step_machine": best_step_machine,
        "halting_machines": halted_machines,
        "non_halting_machines": non_halted_machines,
        "total_machines": total_machines,
    }

    return results

async def get_progress():
    while True:
        progress = await progress_queue.get()
        yield progress
        if progress >= 100:
            break
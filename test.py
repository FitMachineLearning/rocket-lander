
from environments.rocketlander import RocketLander
import numpy as np
import gym

if __name__ == "__main__":
    # Settings holds all the settings for the rocket lander environment.
    settings = {'Side Engines': True,
                'Clouds': True,
                'Vectorized Nozzle': True,
                'Starting Y-Pos Constant': 1,
                'Initial Force': 'random'}  # (6000, -10000)}

ENVIRONMENT_NAME = "LunarLanderContinuous-v2"
env = gym.make(ENVIRONMENT_NAME)
s = env.reset()

from control_and_ai.pid import PID_Benchmark

# Initialize the PID algorithm
pid = PID_Benchmark()

epsilon = 0.05
total_reward = 0
episode_number = 5

for episode in range(episode_number):
    while (1):
        a = pid.pid_algorithm(s) # pass the state to the algorithm, get the actions
        # Step through the simulation (1 step). Refer to Simulation Update in constants.py
        s, r, done, info = env.step(a)
        total_reward += r   # Accumulate reward
        # -------------------------------------
        # Optional render
        env.render()
        # Draw the target
        # Refresh render

        # When should the barge move? Water movement, dynamics etc can be simulated here.

        # Touch down or pass abs(THETA_LIMIT)
        if done:
            print('Episode:\t{}\tTotal Reward:\t{}'.format(episode, total_reward))
            total_reward = 0
            env.reset()
            break

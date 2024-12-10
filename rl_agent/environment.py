# rl_agent/environment.py
import gym
from gym import spaces
import numpy as np

class SDNEnvironment(gym.Env):
    def __init__(self):
        super(SDNEnvironment, self).__init__()

        # Action space: 4 possible routing paths
        self.action_space = spaces.Discrete(4)

        # Observation space: network state (e.g., traffic loads, delays)
        self.observation_space = spaces.Box(low=0, high=100, shape=(5,), dtype=np.float32)

        # Internal state
        self.state = None
        self.steps = 0
        self.max_steps = 50  # Max steps per episode

    def reset(self):
        """Reset the environment state to an initial value."""
        self.state = np.random.randint(0, 100, size=(5,))
        self.steps = 0
        return self.state

    def step(self, action):
        """Simulate the effect of an action on the environment."""
        self.state = self.state - (action * np.random.randint(1, 10, size=(5,)))
        reward = -np.sum(self.state)  # Reward: minimize total network load
        latency_penalty = np.mean(self.state) / 10
        packet_loss_penalty = np.random.uniform(0, 5)
        reward -= (latency_penalty + packet_loss_penalty)

        self.steps += 1
        done = self.steps >= self.max_steps  # Episode ends after max steps
        return self.state, reward, done, {}

    def render(self, mode="human"):
        """Optional visualization of the environment state."""
        print(f"Current State: {self.state}")

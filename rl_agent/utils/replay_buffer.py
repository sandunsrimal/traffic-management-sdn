# rl_agent/utils/replay_buffer.py
import numpy as np
from collections import deque

class ReplayBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def add(self, experience):
        """Add a new experience to the buffer."""
        self.buffer.append(experience)

    def sample(self, batch_size):
        """Sample a batch of experiences from the buffer."""
        if batch_size > len(self.buffer):
            raise ValueError("Batch size exceeds buffer length.")
        indices = np.random.choice(len(self.buffer), batch_size, replace=False)
        return [self.buffer[idx] for idx in indices]

    def __len__(self):
        """Return the current size of the buffer."""
        return len(self.buffer)

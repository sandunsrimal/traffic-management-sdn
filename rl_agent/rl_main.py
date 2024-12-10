# rl_agent/rl_main.py
import os
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.logger import configure
from environment import SDNEnvironment

MODEL_PATH = "models/dqn_model"
LOG_DIR = "./logs/"

def train_agent():
    # Initialize the custom SDN environment
    env = SDNEnvironment()

    # Create a DQN agent
    model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, buffer_size=50000, batch_size=64)

    # Configure logging
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = configure(LOG_DIR, ["stdout", "tensorboard"])
    model.set_logger(logger)

    # Add evaluation callback
    eval_callback = EvalCallback(env, best_model_save_path="./models/",
                                  log_path="./logs/", eval_freq=1000)

    # Train the model
    print("Training RL Agent...")
    model.learn(total_timesteps=20000, callback=eval_callback)

    # Save the model
    os.makedirs("models", exist_ok=True)
    model.save(MODEL_PATH)
    print(f"Model saved at {MODEL_PATH}")

def evaluate_agent():
    # Load the custom SDN environment
    env = SDNEnvironment()

    # Load the trained model
    if not os.path.exists(MODEL_PATH + ".zip"):
        raise FileNotFoundError("Model file not found. Train the agent first.")
    model = DQN.load(MODEL_PATH)

    # Evaluate the agent
    obs = env.reset()
    done = False
    total_reward = 0

    print("Evaluating RL Agent...")
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        total_reward += reward
        env.render()

    print(f"Total Reward: {total_reward}")

if __name__ == "__main__":
    mode = input("Choose mode (train/evaluate): ").strip().lower()
    if mode == "train":
        train_agent()
    elif mode == "evaluate":
        evaluate_agent()
    else:
        print("Invalid mode. Please choose 'train' or 'evaluate'.")

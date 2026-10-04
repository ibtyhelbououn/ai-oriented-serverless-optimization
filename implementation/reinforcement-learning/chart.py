import matplotlib.pyplot as plt

episodes = range(1, 1001)
rewards = [sum_reward / episode for episode, sum_reward in enumerate(cumulative_rewards, 1)]

plt.plot(episodes, rewards)
plt.title("Reward Convergence Over Episodes")
plt.xlabel("Episodes")
plt.ylabel("Cumulative Reward")
plt.grid()
plt.show()

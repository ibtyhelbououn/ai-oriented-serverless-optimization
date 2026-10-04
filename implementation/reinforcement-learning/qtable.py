import matplotlib.pyplot as plt

# Simulated Q-values over training episodes (sampled every 100 episodes)
episodes = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
q_low_scale_up =    [0.0, 0.0056, 0.9584, 2.1724, 3.0153, 3.7572, 5.4472, 6.1756, 6.3365, 6.7438]
q_low_scale_down =  [0.0, 3.8636, 6.0219, 7.5249, 8.4684, 9.0460, 9.3821, 9.6219, 9.7686, 9.8575]
q_high_scale_up =   [0.1, 3.7246, 6.0528, 7.5673, 8.4867, 9.0526, 9.4071, 9.6258, 9.7679, 9.8599]
q_high_scale_down = [0.0, 0.2555, 1.7777, 2.5089, 4.0511, 5.0233, 5.4708, 6.1868, 6.6182, 6.7381]

plt.figure(figsize=(10, 6))
plt.plot(episodes, q_low_scale_up, label='Q(low_load, scale_up)', marker='o')
plt.plot(episodes, q_low_scale_down, label='Q(low_load, scale_down)', marker='o')
plt.plot(episodes, q_high_scale_up, label='Q(high_load, scale_up)', marker='o')
plt.plot(episodes, q_high_scale_down, label='Q(high_load, scale_down)', marker='o')

plt.title("Q-table Convergence Over Training Episodes")
plt.xlabel("Episode")
plt.ylabel("Q-value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

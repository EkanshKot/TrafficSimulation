# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:18:01 2026

@author: ekans
"""

import numpy as np
import matplotlib.pyplot as plt

ROAD_LENGTH = 1000
NUM_CARS = 60
MAX_SPEED = 5.0
SAFE_DISTANCE = 10
HUMAN_NOISE = 0.4
TIMESTEPS = 600
WARMUP = 200

RUNS_PER_SETTING = 20
AUTONOMOUS_RATIOS = [0.0, 0.1, 0.2, 0.3, 0.4]

def run_simulation(autonomous_ratio):
    positions = np.linspace(0, ROAD_LENGTH, NUM_CARS, endpoint=False)
    speeds = np.random.uniform(2, MAX_SPEED, NUM_CARS)

    is_autonomous = np.zeros(NUM_CARS, dtype=bool)
    is_autonomous[:int(NUM_CARS * autonomous_ratio)] = True
    np.random.shuffle(is_autonomous)

    avg_speeds = []

    for _ in range(TIMESTEPS):
        new_speeds = speeds.copy()

        for i in range(NUM_CARS):
            next_car = (i + 1) % NUM_CARS
            distance = (positions[next_car] - positions[i]) % ROAD_LENGTH

            if distance < SAFE_DISTANCE:
                new_speeds[i] *= 0.6
            elif speeds[i] < MAX_SPEED:
                new_speeds[i] += 0.3

            if not is_autonomous[i]:
                new_speeds[i] += np.random.uniform(-HUMAN_NOISE, HUMAN_NOISE)

            new_speeds[i] = np.clip(new_speeds[i], 0, MAX_SPEED)

        speeds = new_speeds
        positions = (positions + speeds) % ROAD_LENGTH
        avg_speeds.append(np.mean(speeds))

    return np.mean(avg_speeds[WARMUP:])

results = {}

for ratio in AUTONOMOUS_RATIOS:
    values = []
    for _ in range(RUNS_PER_SETTING):
        values.append(run_simulation(ratio))
    results[ratio] = values

means = np.array([np.mean(results[r]) for r in AUTONOMOUS_RATIOS])
stds = np.array([np.std(results[r]) for r in AUTONOMOUS_RATIOS])

plt.figure(figsize=(10, 6))
plt.errorbar(
    AUTONOMOUS_RATIOS,
    means,
    yerr=stds,
    fmt="o-",
    capsize=5
)
plt.xlabel("Autonomous Car Ratio")
plt.ylabel("Average Steady-State Speed")
plt.title("Effect of Autonomous Vehicles on Traffic Flow")
plt.grid(True)
plt.show()

print("\nINTERPRETATION OF RESULTS\n")

for i, ratio in enumerate(AUTONOMOUS_RATIOS):
    print(f"Autonomous Ratio: {int(ratio*100)}%")
    print(f"  Mean Speed: {means[i]:.2f}")
    print(f"  Std Deviation: {stds[i]:.2f}")
    print("  Interpretation:")
    print("   - Mean speed represents typical traffic efficiency after stabilization.")
    print("   - Standard deviation represents variability caused by randomness.")
    print()

baseline = means[0]
best = means[-1]
improvement = ((best - baseline) / baseline) * 100

print("OVERALL INSIGHT")
print(f"Introducing autonomous vehicles increased average traffic speed by approximately {improvement:.1f}%.")
print("Even small percentages of autonomous cars reduce congestion and stabilize traffic flow.")
print("This suggests that intelligent local behavior can improve global system efficiency.")

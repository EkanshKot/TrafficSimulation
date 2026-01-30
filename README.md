# TrafficSimulation
Hi Guys! looking to Share a Project I made a while ago,This project showcases an agent-based simulation designed to explore how autonomous vehicles impact traffic efficiency. In this simulation, vehicles act as autonomous agents navigating a circular road, adhering to local rules for acceleration, braking, and maintaining following distances.  


# Traffic Flow Simulation with Autonomous Vehicles

This project simulates traffic flow on a circular road to study how introducing autonomous vehicles affects overall traffic efficiency.

##  Overview
The model represents cars as agents that follow simple local rules:
- Maintain safe distance
- Accelerate when possible
- Decelerate when too close

Human drivers introduce randomness, while autonomous vehicles behave deterministically.They Behave according to a certaun set rules

The simulation measures how increasing the fraction of autonomous vehicles impacts average steady-state traffic speed.


---

## ⚙️ Simulation Parameters,For eg
| Parameter | Description |
|--------|------------|
| Road length | 1000 units |
| Number of cars | 60 |
| Max speed | 5.0 |
| Safe distance | 10 |
| Human noise | ±0.4 |
| Timesteps | 600 |
| Warmup | First 200 steps ignored |

---

##  Experiment Design
- Autonomous ratios tested: 0% → 40%
- 20 independent runs per setting
- Results averaged to reduce randomness

---

##  Output
- Error-bar plot showing average speed vs autonomous ratio
- Console-based statistical interpretation
- Overall percentage improvement calculation

---

##  Results Summary
- Mean traffic speed increases with autonomous vehicle ratio
- Variability decreases as autonomous cars reduce stop-and-go waves
- Even small penetration rates yield measurable benefits


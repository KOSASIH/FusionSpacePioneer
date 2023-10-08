import numpy as np
import matplotlib.pyplot as plt

def simulate_fusion_reactor_performance(power_output, efficiency):
    """
    Simulates the performance and efficiency of a fusion reactor design for interstellar travel.
    
    Parameters:
    - power_output (float): The fusion reactor's power output in watts.
    - efficiency (float): The efficiency of the fusion reactor.
    
    Returns:
    - travel_time (float): The estimated travel time in years.
    """
    # Constants
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    c = 299792458  # Speed of light in m/s
    
    # Inputs
    distance = 4.22 * 9.461e+15  # Distance to the target star system in meters (e.g., Proxima Centauri)
    velocity = 0.1 * c  # Spacecraft's velocity in m/s
    
    # Calculate the required fusion power based on inputs
    mass = power_output / (efficiency * c**2)
    
    # Calculate the acceleration and travel time
    acceleration = power_output / (mass * velocity)
    travel_time = np.sqrt(2 * distance / acceleration) / (365 * 24 * 60 * 60)  # Convert seconds to years
    
    return travel_time

# Example usage
power_output = 1e12  # Fusion reactor's power output in watts
efficiency = 0.1  # Efficiency of the fusion reactor

travel_time = simulate_fusion_reactor_performance(power_output, efficiency)
print(f"Estimated travel time: {travel_time:.2f} years")

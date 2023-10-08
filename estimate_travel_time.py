import math

def estimate_travel_time(distance, velocity, fusion_power):
    # Calculate the acceleration using fusion power and spacecraft mass
    spacecraft_mass = 1000  # kg (example value)
    acceleration = fusion_power / spacecraft_mass
    
    # Calculate the time to reach the target star system
    time = math.sqrt((2 * distance) / acceleration)
    
    # Convert time to years
    travel_time_years = time / (365 * 24 * 60 * 60)
    
    return travel_time_years

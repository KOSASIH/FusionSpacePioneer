def calculate_fusion_power(mass, velocity, efficiency):
    # Convert mass to kilograms
    mass_kg = mass * 1000  # Assuming mass is given in metric tons

    # Convert velocity to meters per second
    velocity_mps = velocity * 1000  # Assuming velocity is given in kilometers per second

    # Calculate kinetic energy
    kinetic_energy = 0.5 * mass_kg * velocity_mps**2

    # Calculate required fusion power
    fusion_power = kinetic_energy / efficiency

    return fusion_power

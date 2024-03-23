"""
Author: Parisa Arbab
Date: March 17, 2024,
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link: https://youtu.be/HQl1obXO6UE

answered this question in the above link:
• How efficient is your simulation?  Can you do better?
• When computing the average distance between planets, would it be better to sample random
days rather than iterating over every day for 1000 years?
• What was your original assumption regarding the closest planet to Earth?  Did the results match
your expectation?  Does the definition of “closest” matter?


"""
import math

class Planet:
    """Represents a planet with a given radius and orbital period."""
    def __init__(self, name, radius, year):
        """Initialize a Planet object with the given name, radius, and year."""
        self.name = name
        self.radius = radius
        self.year = year

    def position(self, day):
        """Calculate the position of the planet on a specific day relative to the Sun."""
        angle = (day / self.year) * 2 * math.pi
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        return round(x, 2), round(y, 2)

def distance(planet1, planet2, day):
    """Calculate the distance between two planets on a specific day."""
    pos1 = planet1.position(day)
    pos2 = planet2.position(day)
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def simulate_solar_system(planets):
    total_days = 365000
    distances_matrix = {planet1.name: {planet2.name: 0 for planet2 in planets} for planet1 in planets}

    for day in range(1, total_days + 1):
        for i, planet1 in enumerate(planets):
            for planet2 in planets[i+1:]:
                dist = distance(planet1, planet2, day)
                distances_matrix[planet1.name][planet2.name] += dist
                distances_matrix[planet2.name][planet1.name] += dist

    # Calculating the average distances
    for planet1 in distances_matrix:
        for planet2 in distances_matrix[planet1]:
            distances_matrix[planet1][planet2] /= total_days

    # Printing the 8x8 chart
    print("Average distances between planets over 365000 days (units):")
    print(f"{'':<10}", end="")
    for planet in planets:
        print(f"{planet.name:<10}", end="")
    print()

    for planet1 in planets:
        print(f"{planet1.name:<10}", end="")
        for planet2 in planets:
            print(f"{distances_matrix[planet1.name][planet2.name]:<10.2f}", end="")
        print()

# Example usage
planets = [
    Planet("Mercury", 3.5, 88),
    Planet("Venus", 6.7, 225),
    Planet("Earth", 9.3, 365),
    Planet("Mars", 14.2, 687),
    Planet("Jupiter", 48.4, 4333),
    Planet("Saturn", 88.9, 10759),
    Planet("Uranus", 179, 30687),
    Planet("Neptune", 288, 60190),
]

simulate_solar_system(planets)

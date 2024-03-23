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
        """
        Calculate the position of the planet on a specific day relative to the Sun.

        Parameters:
        - day (int): The day for which to calculate the position.

        Returns:
        - tuple: The x and y coordinates of the planet's position.
        """
        angle = (day / self.year) * 2 * math.pi
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        return round(x, 2), round(y, 2)

def distance(planet1, planet2, day):
    """
    Calculate the distance between two planets on a specific day.

    Parameters:
    - planet1 (Planet): The first planet object.
    - planet2 (Planet): The second planet object.
    - day (int): The day for which to calculate the distance.

    Returns:
    - float: The distance between the two planets on the given day.
    """
    pos1 = planet1.position(day)
    pos2 = planet2.position(day)
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def simulate_solar_system(planets):
    total_days = 365000
    earth = next(planet for planet in planets if planet.name == "Earth")
    earth_distances = {planet.name: 0 for planet in planets if planet.name != "Earth"}

    for day in range(1, total_days + 1):
        for planet in planets:
            if planet.name != "Earth":
                earth_distances[planet.name] += distance(earth, planet, day)

    avg_distances = {planet: total_distance / total_days for planet, total_distance in earth_distances.items()}
    closest_planet = min(avg_distances, key=avg_distances.get)

    print(f"Average distances to Earth over {total_days} days:")
    for planet, avg_distance in avg_distances.items():
        print(f"{planet}: {avg_distance:.2f} units")

    print(f"\nThe closest planet to Earth is {closest_planet} with an average distance of {avg_distances[closest_planet]:.2f} units.")




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

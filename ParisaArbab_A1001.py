"""
Author: Parisa Arbab
Date: March 17, 2024,
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/DsjJKq5wB3s

answered this question in the above link:

1.What is the distance between Earth and Mars on day 732? 6.52
2. How does your position() function work?  What trigonometry functions did you need to use?
3. How does your distance() function work?  Show that you employed top-down design in its implementation.

"""
import math


class Planet :
    """Represents a planet with a given radius and orbital period."""

    def __init__(self, radius, year) :
        """Initialize a Planet object with the given radius and year."""
        self.radius = radius
        self.year = year
    #question 2
    def position(self, day) :
        """
        Calculate the position of the planet on a specific day relative to the Sun.

        Parameters:
        - day (int): The day for which to calculate the position.

        Returns:
        - tuple: The x and y coordinates of the planet's position.
        """
        angle = (day / self.year) * 2 * math.pi
        x = self.radius * math.cos ( angle )
        y = self.radius * math.sin ( angle )
        return round ( x, 2 ), round ( y, 2 )

#question 3
def distance(planet1, planet2, day) :
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
    distance = math.sqrt((pos1[0 ] - pos2[0 ]) ** 2 + (pos1[1 ] - pos2[1 ]) ** 2 )
    return round(distance, 2 )


# Define planets with their orbital radius and year length
mercury = Planet(3.5, 88 )
venus = Planet(6.7, 225 )
earth = Planet(9.3, 365 )
mars = Planet(14.2, 687 )
jupiter = Planet(48.4, 4333 )
saturn = Planet(88.9, 10759 )
uranus = Planet(179, 30687 )
neptune = Planet(288, 60190 )


print("Mercury's position on day 0:", mercury.position(0))
print("Mercury's position on day 22:", mercury.position(22))
print("Mercury's position on day 33:", mercury.position(33))
print("Mercury's position on day 440:", mercury.position(440))

# Calculate the distance between Earth and Mars on day 732
#question 1
d = distance(earth, mars, 732)
print("distance between Earth and Mars on day 732 = ", d)


# Ask the user to enter the names of the two planets and the day
planet1_name = input("Enter the name of the first planet: ")
planet2_name = input("Enter the name of the second planet: ")
day = int(input("Enter the day: "))

# Create a dictionary to map planet names to their corresponding Planet objects
planets = {
    "mercury": mercury,
    "venus": venus,
    "earth": earth,
    "mars": mars,
    "jupiter": jupiter,
    "saturn": saturn,
    "uranus": uranus,
    "neptune": neptune
}

# Get the Planet objects corresponding to the names entered by the user
planet1 = planets.get(planet1_name.lower())
planet2 = planets.get(planet2_name.lower())

# Check if the planets exist
if planet1 is None or planet2 is None:
    print("One or both of the planets entered do not exist.")
else:
    # Calculate the distance between the two planets on the given day
    d = distance(planet1, planet2, day)
    print(f"Distance between {planet1_name} and {planet2_name} on day {day} is {d}")





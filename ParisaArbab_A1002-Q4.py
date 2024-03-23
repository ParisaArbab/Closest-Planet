"""
Author: Parisa Arbab
Date: March 17, 2024,
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:

answered this question in the above link:

1.How efficient is your simulation?  Can you do better?
2.When computing the average distance between planets, would it be better to sample random
days rather than iterating over every day for 1000 years?
3.What was your original assumption regarding the closest planet to Earth?  Did the results match
your expectation?  Does the definition of “closest” matter?

"""

import math
import pandas as pd
import matplotlib.pyplot as plt


class Planet :
    """
       Represents a planet with a specific orbital radius and period.
       """
    def __init__(self, name, radius, year) :
        """
               Initializes a new Planet instance.

               Parameters:
               - name (str): The name of the planet.
               - radius (float): The orbital radius of the planet (in arbitrary units).
               - year (int): The orbital period of the planet (in Earth days).
               """
        self.name = name
        self.radius = radius
        self.year = year

    def position(self, day) :
        """
               Calculates the position of the planet on a given day.

               Parameters:
               - day (int): The day for which to calculate the planet's position.

               Returns:
               - tuple: The (x, y) coordinates of the planet's position.
               """
        angle = (day / self.year) * 2 * math.pi
        x = self.radius * math.cos ( angle )
        y = self.radius * math.sin ( angle )
        return round ( x, 2 ), round ( y, 2 )


def distance(planet1, planet2, day) :
    """
    Calculates the distance between two planets on a given day.

    Parameters:
    - planet1 (Planet): The first planet object.
    - planet2 (Planet): The second planet object.
    - day (int): The day for which to calculate the distance.

    Returns:
    - float: The distance between the two planets.
    """
    pos1 = planet1.position ( day )
    pos2 = planet2.position ( day )
    return math.sqrt ( (pos1[ 0 ] - pos2[ 0 ]) ** 2 + (pos1[ 1 ] - pos2[ 1 ]) ** 2 )


def record_distances(planets, days=1000) :
    """
       Records the distances from Earth to Mercury, Venus, and Mars over a given number of days.

       Parameters:
       - planets (list of Planet): The list of planets in the simulation.
       - days (int): The number of days over which to record distances.
       """
    # Create a list for each planet of interest
    distances = {"Mercury" : [ ], "Venus" : [ ], "Mars" : [ ]}
    earth = next ( planet for planet in planets if planet.name == "Earth" )

    # Loop over each day, recording distances
    for day in range ( 1, days + 1 ) :
        for key in distances.keys () :
            other_planet = next ( planet for planet in planets if planet.name == key )
            # Record the distance for the day
            distances[ key ].append ( distance ( earth, other_planet, day ) )

    # Convert the lists to a Pandas DataFrame
    df = pd.DataFrame ( distances )
    df.to_csv ( "planet_distances.csv", index=False )


# Define the planets as before
planets = [ Planet ( "Mercury", 3.5, 88 ), Planet ( "Venus", 6.7, 225 ), Planet ( "Earth", 9.3, 365 ),
            Planet ( "Mars", 14.2, 687 ), Planet ( "Jupiter", 48.4, 4333 ), Planet ( "Saturn", 88.9, 10759 ),
            Planet ( "Uranus", 179, 30687 ), Planet ( "Neptune", 288, 60190 ) ]

# Record the distances
record_distances ( planets )

# Load the recorded distances
df = pd.read_csv("planet_distances.csv")

# Plot the distances over time using Matplotlib
plt.figure(figsize=(14, 7))
plt.plot(df.index, df["Mercury"], label="Mercury")
plt.plot(df.index, df["Venus"], label="Venus")
plt.plot(df.index, df["Mars"], label="Mars")
plt.title("Distance from Earth over 1000 Days")# Chart title
plt.xlabel("Day") # X-axis label
plt.ylabel("Distance (units)") # Y-axis label
plt.legend()# Show legend
plt.show()# Display the plot


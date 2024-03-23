# Closest-Planet
A1001: calculate distance between planets on a specific days
A1002-Q1: top-down design structure for ave distance of Earth and other planets on 1000 earth year
A1002-Q2: simulate average distance of Earth with other planets on 1000 Earth year and represent in a 8*8 chart
A1002-Q3: simulate average distance of Earth with other planets on 1000 Earth year and represent the closest planet to earth
A1002-Q4: simulate average distance of Earth with 3 other planets on 1000 day and represent, create 3 time series for them, show the plot, and save the result on a csv file. 
Explain A1002-Q4:
this code defines a simple model for calculating the orbital positions of planets and uses this model to record and plot the distances from Earth to Mercury, Venus, and Mars over 1000 days. It demonstrates the application of basic physics and mathematics principles in a Python program, enhanced with data manipulation using Pandas and visualization with Matplotlib.


Importing Libraries
math: Used for mathematical operations like square root and trigonometric functions.
pandas: A data manipulation and analysis library. It's used here to create a DataFrame (a tabular data structure) and save it to a CSV file.
matplotlib.pyplot: A plotting library used for creating static, interactive, and animated visualizations in Python.
Class Definition: Planet
This class represents a planet in the solar system. Each planet has a name, an orbital radius (the average distance from the Sun), and an orbital period (the time it takes to complete one orbit around the Sun, measured in Earth days).
The __init__ method initializes a Planet object with its name, radius, and year.
The position method calculates the planet's position in space on a given day relative to the Sun. It uses simple circular motion equations, assuming circular orbits for simplicity. The position is represented by (x, y) coordinates, calculated using trigonometric functions.
Function: distance
This function calculates the distance between two planets on a specific day. It uses the Pythagorean theorem to calculate the distance between two points in 2D space, based on the positions of the two planets.
Function: record_distances
This function simulates the solar system for a specified number of days (default is 1000 days). It records the distances between Earth and Mercury, Venus, and Mars for each day.
It creates a dictionary distances to store lists of daily distances for each of the three planets of interest.
For each day, it calculates the distances from Earth to each of the three planets and appends these distances to the respective lists in the distances dictionary.
Finally, it converts the dictionary of distances into a pandas.DataFrame and saves it as a CSV file named "planet_distances.csv". This file contains 1000 rows (one for each day) and 3 columns (one for each planet), representing the daily distances.
Main Execution Block
A list of Planet objects is created, including Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune, each initialized with their name, orbital radius, and orbital period.
The record_distances function is called with this list of planets, which performs the simulation and records the distances.
After recording the distances, the data is read from "planet_distances.csv" into a pandas.DataFrame named df.
Using matplotlib.pyplot, the distances from Earth to Mercury, Venus, and Mars are plotted over the 1000-day period. Each planet's distance is shown as a separate line in the plot.
The plot includes a title, labels for the x-axis (Day) and y-axis (Distance in arbitrary units), and a legend to distinguish between the planets.
This code effectively demonstrates how to model simple astronomical phenomena and visualize the results using Python.







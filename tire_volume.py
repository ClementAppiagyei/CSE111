import math
from datetime import date

# Ask the user for some information.
width = float(input("Enter the width of the tire in mm: "))
ratio = float(input("Enter the ratio: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the volume.
volume = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

# Round the volume to 2 dp.
volume = round(volume, 2)

# Get the current date (YYYY-MM-DD).
current_date = date.today()

# Open the file and append the data.
with open("volumes.txt", "a") as f:
    f.write(f"{current_date}, {width}, {ratio}, {diameter}, {volume}\n")

# Print the result.
print(f"The approximate volume is {volume} liters")
print(f"Data saved to volumes.txt")
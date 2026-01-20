"""
This program is to calculate and print fuel efficiency in
both miles per gallon and liters per 100 kilometers.
"""

# Define the main function of the program to receive input from the user and print
def main():
    """
    The program to receive input from the user and print
    """

    start_miles = float(input("Enter the first odometer reading (miles): "))
    end_miles = float(input("Enter the second odometer reading (miles): "))
    amount_gallon = float(input("Enter the amount of fuel used (gallons): "))


    mpg = miles_per_gallon(start_miles, end_miles, amount_gallon)
    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallon):
    """
    Compute and return the average number of miles that a vehicle
    traveled per gallon of fuel.
    Parameters
    start_miles: An odometer value in miles.
    end_miles: Another odometer value in miles.
    amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """

    # Calculate the miles per gallon
    mpg = (end_miles - start_miles) / amount_gallon

    return mpg

def lp100k_from_mpg(mpg):
    """
    Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    lp100k = 235.215 / mpg

    return lp100k

# Call the function to be executed
main()
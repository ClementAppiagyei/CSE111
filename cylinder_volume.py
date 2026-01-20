import math

# def print_cylinder_volume():
#     """
#     Compute the volume of a right circular cylinder and 
#     then prints the volume for the user to see
#     """

#     # Get the radius and the height from the user.
#     radius = float(input("Enter the radius of the cylinder: "))
#     height = float(input("Enter the height of the cylinder: "))

#     # Compute the volume of a circular cylinder
#     volume = math.pi * radius ** 2 * height
    
#     # Prints the volume for the user to see.
#     print(f"The volume of the circular cylinder is {volume:.2f}")

#     # Call the function
# print_cylinder_volume()


# def print_cylinder_volume(radius, height):
#     """
#     The program gets input through its 
#     two parameters named radius and height.
#     """

#     # Compute the volume of the cylinder.
#     volume = math.pi * radius ** 2 * height

#     # Round the volume
#     # rounded_volume = (volume, 2)

#     # Print the volume of the cylinder.
#     print(volume)

# # Call the function
# print_cylinder_volume(2.3, 4.5)


def compute_cylinder_volume(radius, height):
    """
    This program returns the volume instead of printing it.
    """

    # Compute the volume of the cylinder.
    volume = math.pi * radius ** 2 * height

    # Return the volume of the cylinder to the program.
    return volume

# Call the function
volume = compute_cylinder_volume(2.5, 4.1)
print(volume)
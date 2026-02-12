# Receipt Program
# Additional functionality added: formatted receipt alignment
# and clean currency formatting.

import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """
    Reads the contents of a CSV file into a dictionary.
    The dictionary key is the value at key_column_index.
    The value is the entire row as a list, but the price
    is converted to a float.
    """
    products_dict = {}

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            key = row[key_column_index]

            # Convert price to float (price is last column)
            row[-1] = float(row[-1])

            products_dict[key] = row

    return products_dict


def main():
    try:
        # Store name
        store_name = "Danis Grocery Store"
        print(store_name)

        # Read products dictionary
        products = read_dictionary("products.csv", 0)

        total_items = 0
        subtotal = 0

        # Open request file
        with open("request.csv", "r", newline="") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header

            print("\nRequested Items:")

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                product = products[product_number]

                # Determine name and price positions
                if len(product) == 2:
                    name = product[0]
                    price = product[1]
                else:
                    name = product[1]
                    price = product[2]

                item_total = price * quantity

                total_items += quantity
                subtotal += item_total

                print(f"{name}: {quantity} @ ${price:.2f}")

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")

        # Sales tax 6%
        tax = subtotal * 0.06
        print(f"Sales Tax: ${tax:.2f}")

        total = subtotal + tax
        print(f"Total: ${total:.2f}")

        print("\nThank you for shopping with us!")

        # Current date and time
        current_date_time = datetime.now()
        print(current_date_time.strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError:
        print("Error: missing file")
    except PermissionError:
        print("Error: permission denied")
    except KeyError as key_error:
        print(f"Error: unknown product ID {key_error}")


if __name__ == "__main__":
    main()

import csv
from datetime import datetime

PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

PRODUCT_QUANTITY_INDEX = 1

FILE_NAME_PRODUCTS = 'products.csv'
FILE_NAME_REQUEST = 'request.csv'


def read_products(products):
    dictionary = {}
    with open(products, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            key = row[PRODUCT_ID_INDEX]
            dictionary[key] = [row[PRODUCT_NAME_INDEX], float(row[PRODUCT_PRICE_INDEX])]

    return dictionary


def main():
    try:
        products = read_products(FILE_NAME_PRODUCTS)

        print('Inkom Emporium')
        print()

        number_of_items = 0
        subtotal = 0
        tax_percent = 0.06

        with open(FILE_NAME_REQUEST) as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                product_name = products[row[PRODUCT_ID_INDEX]][0]
                product_price = products[row[PRODUCT_ID_INDEX]][1]

                number_of_items += int(row[PRODUCT_QUANTITY_INDEX])
                subtotal += product_price * int(row[PRODUCT_QUANTITY_INDEX])

                print(f'{product_name}: {product_price} @ {row[PRODUCT_QUANTITY_INDEX]}')

        tax = subtotal * tax_percent
        total = subtotal + tax
        current_date_and_time = datetime.now()

        print()
        print(f'Number of Items: {number_of_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {tax:.2f}')
        print(f'Total: {total:.2f}')

        print()
        print('Thank you for shopping at the Inkom Emporium.')
        print(f'{current_date_and_time:%a %b %d %H:%M:%S %Y}')
    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except KeyError as error:
        print(error)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()

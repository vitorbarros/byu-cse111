import pathlib


def provinces():
    file_name = 'provinces.txt'
    file_full_path = f'{pathlib.Path().resolve()}/{file_name}'

    items_list = []
    items_alberta_list = []
    with open(file_full_path, 'rt') as file:
        for line in file:
            clean_line = line.strip()

            if clean_line == 'AB':
                items_alberta_list.append('Alberta')
                items_list.append('Alberta')

            else:
                items_list.append(clean_line)

    # full list
    print('full list')
    print(items_list)
    print()

    # no first item
    items_list.pop(0)
    print('no first item')
    print(items_list)
    print()

    # alberta count
    print('Alberta quantity')
    print(len(items_alberta_list))


def main():
    provinces()


if __name__ == '__main__':
    main()

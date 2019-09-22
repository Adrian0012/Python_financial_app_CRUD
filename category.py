from pathlib import Path


category_path = Path('C:/Users/__me__/Desktop/APP')


def create_category():
    try:
        #select_year = input('Please select the financial Year: ')
        #select_month = input('Please specify the month: ')
        name = input('Please create a Category: \n')
        filename = category_path.joinpath(name + '.txt')
        print('Category [{}] has been created!'.format(name))
        with open(filename, 'x') as file:
            file.close()
        while name != category_path:
            break
    except FileExistsError:
        print('Category already exists!! // Please create a new category!')


def view_category():
    for filename in category_path.iterdir():
        print(filename.stem)


def update_file():
    category_name = input(
        'Please choose the Category you would like to Update OR Press [Q] to return to the Main Menu: \n')
    category_name = category_name.lower().strip()
    filename = category_path.joinpath(category_name + '.txt')

    while category_name != 'q':
        if category_name == 'q':
            break
        if not filename.is_file():
            print('File does not exist! Please chose an existing file!')
            break

        with open(filename, 'a') as file:
            file.write(input('Type here: ') + '\n')
            file.close()

        print('Would you like to add more data? [Y]es or [N]o ')
        x = input('>')
        x = x.lower().strip()
        if x == 'y':
            continue
        elif x == 'n':
            break


def read_file():
    name = input('Please chose the category you want to open! \n')
    name = name.lower().strip()
    filename = category_path.joinpath(name + '.txt')
    try:
        with open(filename, 'r') as read:
            for idx, lines in enumerate(read, 1):
                lines = lines.strip('\n')
                print(idx, lines)
        while name != category_path:
            break
    except FileNotFoundError:
        print('File does not exist! Please select a valid category!')


def delete_data():
    pass
# TODO delete selected data from a file

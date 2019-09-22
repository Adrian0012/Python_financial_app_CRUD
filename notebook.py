from pathlib import Path


category_path = Path('C:/Users/__me__/Desktop/APP')

def select_folder():
    select_year = input('Year: ')
    select_month = input('Month: ')
    category_name = input('File: ')
    filename = category_path.joinpath(select_year, select_month, category_name + '.txt')


    with open(filename, 'a') as file:
        file.write(input('Type here: ') + '\n')
        file.close()


select_folder()

def update_file():
    category_name = input(
        'Please choose the Category you would like to Update OR Press [Q] to return to the Main Menu: \n')
    category_name = category_name.lower().strip()
    filename = category_path.joinpath(category_name + '.txt')
    # TODO check the while and if statement // it may not be required to to have them both
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

import category


def main():
    header()
    menu()


def header():
    print("""
                    ---------------------------------------
                    ---------Financial Application---------
                    ---------------------------------------""")


def menu():
    while True:

        print("""
        Press [1] to Create a Category          Press [2] to View Categories       
        Press [3] to Update Categories          Press [4] to Read Category Data
        Press [5] to Delete Category Data       Press [Q] to close APP
        
        """)

        cmd = input('Please Select an Option!: \n')
        cmd = cmd.lower().strip()

        if cmd == '1':
            category.create_category()

        elif cmd == '2':
            category.view_category()

        elif cmd == '3':
            category.update_file()

        elif cmd == '4':
            category.read_file()

        elif cmd == '5':
            category.delete_data()

        elif cmd == 'q':
            print('Closing APP....')
            break


if __name__ == "__main__":
    main()

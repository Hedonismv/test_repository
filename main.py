import program.req_downloading as p


def main():
    """Function init the take_url and takes the arguments url and behavior"""
    user_choice = int(input('Choice: '))
    if user_choice == 1:
        input_url = input('Enter the url: ')
        try:
            behavior = int(input('Enter the mode: \n'
                                 '1 - Rewrite\n'
                                 '2 - Add with rename\n'
                                 '3 - Cancel if file exists\n'))
        except ValueError as e:
            print(f"{e} Need the int")
            main()
        if behavior != 1 and behavior != 2 and behavior != 3:
            print(f"Sorry, need only 1 - 2 - 3 integers, you put {behavior}")
            main()
        else:
            p.take_url(input_url, behavior)
    if user_choice == 2:
        path_to_file = str(input('Inter the path to file: '))
        p.check_path(path_to_file)


if __name__ == '__main__':
    main()

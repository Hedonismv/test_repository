import program.req_downloading as p


def main():
    """Function init the take_url and takes the arguments url and behavior"""
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


if __name__ == '__main__':
    main()

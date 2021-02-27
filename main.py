from program.request import take_url


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
    take_url(input_url, behavior)


if __name__ == '__main__':
    main()

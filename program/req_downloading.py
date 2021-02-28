import os
import random
from string import ascii_letters, digits
import requests
import main as m


def take_url(url: str, behavior=1):
    """One of the main function, take the {url} and {behavior} and raise all check functions
            and after raise the main download function - {download_image}"""
    global req
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        print(f"{e}")
        m.main()
    # print('REQ INIT')
    check_url()
    # print('URL CHECKED')
    check_image()
    # print('IMAGE CHECKED')
    check_image_size()
    # print('IMAGE SIZE GOT')
    check_directory()
    return download_image(url, method, behavior)


def check_directory():
    """Check directory with name - image, if this dnt exist , create them else print message"""
    if os.path.exists('image'):
        print('Directory image is exist')
    else:
        os.mkdir('image')
        print('Directory created')


def download_image(url, method=0, behavior=1):
    """Main download function takes URL, method, behavior. Generate name if behavior == 2"""
    split_url = url.split('/')
    filename = split_url[-1]
    # print(filename)  # DEBUG
    print(f"URL1-{url}")
    print(f"METHOD-{method}")
    print(f"BEHAVIOR-{behavior}")
    if method == 1:  # CHUNK DOWNLOAD METHOD
        req = requests.get(url, stream=True)
        print(f"URL-{url}")
        if behavior == 1:  # REWRITE THE FILE
            with open(f'image/{filename}', 'wb') as f:
                for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
                    print('Received a Chunk from 1 method and 1 behavior')  # DEBUG
                    f.write(chunk)
        elif behavior == 2:  # ADD WITH THE RANDOM GENERATED NAME
            if os.path.exists(f'image/{filename}'):
                print('CATCH THE FILE')  # DEBUG
                s_random = random.SystemRandom()
                symbols = ascii_letters + digits
                generated_name = "".join(s_random.choice(symbols) for _ in range(10))  # RANDOM NAME GENERATE
                print(generated_name)
                with open(f'image/{generated_name + filename}', 'wb') as f:
                    for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
                        print('Received a Chunk from 1 method and 2 behavior')  # DEBUG
                        f.write(chunk)
            else:
                with open(f'image/{filename}', 'wb') as f:
                    for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
                        print('Received a Chunk from 1 method and 2 behavior else')  # DEBUG
                        f.write(chunk)
        elif behavior == 3:  # BREAK , COZ FILE IS IN THE DIRECTORY
            print(f'This file is in directory.')
    if method == 2:  # FULL SIZE FILE DOWNLOAD METHOD
        req = requests.get(url)
        if behavior == 1:
            with open(f'image/{filename}', 'wb') as f:
                f.write(req.content)
        elif behavior == 2:
            if os.path.exists(f'image/{filename}'):
                print('CATCH THE FILE')  # DEBUG
                s_random = random.SystemRandom()
                symbols = ascii_letters + digits
                generated_name = "".join(s_random.choice(symbols) for _ in range(10))  # RANDOM NAME GENERATE
                print(generated_name)
                with open(f'image/{generated_name + filename}', 'wb') as f:
                    f.write(req.content)
            else:
                with open(f'image/{filename}', 'wb') as f:
                    for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
                        print('Received a Chunk from 1 method and 2 behavior else')  # DEBUG
                        f.write(chunk)
        elif behavior == 3:  # BREAK , COZ FILE IS IN THE DIRECTORY
            print(f'This file is in directory.')
    else:
        pass


# download_image('https://cdn.pixabay.com/photo/2021/02/15/21/47/robin-6019247_960_720.jpg', 1, 1)


def check_image():
    """Takes content-type from headers and check this, if this image return this, else break script"""
    content_type = req.headers['content-type']
    if content_type[0:5] == 'image':
        print('CATCH IMAGE')
    else:
        raise Exception(f'This url return the {content_type} type, this is not image')


def check_url():
    """Check the status code to the determine if a link exists"""
    status_code = req.status_code
    if status_code == 404:
        print('This site dnt found')
        raise ConnectionError('This site not found! Put the correct url!')
    else:
        print('Link worked')


def check_image_size():
    """This function measures the file size and determines the upload method"""
    global method  # global to function download_image
    image_size = int(req.headers['content-length']) / 1000  # 1 st bytes / 1000 to take kilobytes
    if image_size <= 100:
        print(f'Download in 1 time coz img size is {image_size} kb')
        method = 2  # dif method download
        return method
    else:
        print(f'For chunk download coz img size is {image_size} kb')
        method = 1  # chunk method download
        return method

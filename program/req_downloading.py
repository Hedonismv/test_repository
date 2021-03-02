import os
import random
from string import ascii_letters, digits
import requests
import main as m
from program.config_variables import IMAGES_FORMAT


def check_path(filepath):
    with open(f'{filepath}', 'r') as user_file:
        path_list = []
        for row in user_file:
            path_list.append(row.strip())
    print(path_list)
    for link in path_list:
        print(link)


def take_url(url: str, behavior=1):
    """One of the main function, take the {url} and {behavior} and raise all check functions
            and after raise the main download function - {download_image}"""
    global req
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        print(f"{e}")
        m.main()
    check_url()
    check_image()
    check_image_size()
    check_directory()
    return download_image(url, behavior)


def check_directory():
    """Check directory with name - image, if this dnt exist , create them else print message"""
    if os.path.exists('image'):
        print('Directory image is exist')
    else:
        os.mkdir('image')
        print('Directory created')


def generate_name():
    s_random = random.SystemRandom()
    symbols = ascii_letters + digits
    generated_name = "".join(s_random.choice(symbols) for _ in range(10))  # RANDOM NAME GENERATE
    return generated_name


def download_file(url, filename, generated_name=''):
    with open(f'image/{generated_name + filename}', 'wb') as f:
        if method == 1:
            req = requests.get(url, stream=True)
            for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
                print('Downloading...')
                f.write(chunk)
        elif method == 2:
            req = requests.get(url)
            f.write(req.content)


def download_image(url, behavior=1):
    """Main download function takes URL, method, behavior. Generate name if behavior == 2"""
    split_url = url.split('/')
    filename = split_url[-1]
    if behavior == 1:  # REWRITE THE FILE
        download_file(url, filename)
    elif behavior == 2:  # ADD WITH THE RANDOM GENERATED NAME
        if os.path.exists(f'image/{filename}'):
            download_file(url, filename, generate_name())
        else:
            download_file(filename)
    elif behavior == 3:  # BREAK , COZ FILE IS IN THE DIRECTORY
        print(f'This file is in directory.')
    else:
        pass


# download_image('https://cdn.pixabay.com/photo/2021/02/15/21/47/robin-6019247_960_720.jpg', 1, 1)


def check_image():
    """Takes content-type from headers and check this, if this image return this, else break script"""
    content_type_ns = req.headers['content-type']
    content_type = content_type_ns.split('/')
    cons = content_type[-1]
    if cons in IMAGES_FORMAT:
        print('This is image')
    else:
        raise Exception


def check_url():
    """Check the status code to the determine if a link exists"""
    status_code = req.status_code
    if status_code == 404:
        print('This site dnt found')
        raise ConnectionError('This site not found! Put the correct url!')
    else:
        pass


def check_image_size():
    """This function measures the file size and determines the upload method"""
    global method  # global to function download_image
    image_size = int(req.headers['content-length']) / 1000  # 1 st bytes / 1000 to take kilobytes
    if image_size <= 100:
        method = 2  # dif method download
        return method
    else:
        method = 1  # chunk method download
        return method

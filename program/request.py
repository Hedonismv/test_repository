import requests


def take_url(url: str, mode=1):

    if mode == 1:
        pass  # rewrite file
    if mode == 2:
        pass  # duplicate file
    if mode == 3:
        pass  # break download
    check_url(url)
    check_image(url)
    check_image_size(url)
    return url


def check_image(url):
    req = requests.get(url)
    content_type = req.headers['content-type']
    if content_type[0:5] == 'image':
        print('CATCH IMAGE')
    else:
        print('Cant found and image')


def check_url(url):
    req = requests.get(url)
    status_code = req.status_code
    if status_code == 404:
        print('This site dnt found')
    else:
        print('Link worked')


def check_image_size(url):
    req = requests.get(url)
    image_size = int(req.headers['content-length']) / 1000
    if image_size <= 100:
        print(f'Download in 1 time coz img size is {image_size} kb')
    else:
        print(f'For chunk download coz img size is {image_size} kb')


take_url(
    'https://images.unsplash.com/photo-1614245062871-a28dd5b7566b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D'
    '&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80')

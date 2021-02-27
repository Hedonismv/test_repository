# import requests
# import os
# import random
# from string import ascii_letters, digits
#
#
# def rewrite_file():
#     pass
#
#
# def check_directory():
#     if os.path.exists('../image'):
#         print('Directory image is exist')
#     else:
#         os.mkdir('../image')
#         print('Directory created')
#
#
# check_directory()
#
#
# def download_image(url, method=0, behavior=1):
#     req = requests.get(url, stream=True)
#     split_url = url.split('/')
#     filename = split_url[-1]
#     print(filename)  # DEBUG
#     if method == 1:  # CHUNK DOWNLOAD METHOD
#         if behavior == 1:  # REWRITE THE FILE
#             with open(f'../image/{filename}', 'wb') as f:
#                 for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
#                     print('Received a Chunk')  # DEBUG
#                     f.write(chunk)
#         elif behavior == 2:  # ADD WITH THE RANDOM GENERATED NAME
#             if os.path.exists(f'../image/{filename}'):
#                 print('CATCH THE FILE')  # DEBUG
#                 s_random = random.SystemRandom()
#                 symbols = ascii_letters + digits
#                 generated_name = "".join(s_random.choice(symbols) for _ in range(10))  # RANDOM NAME GENERATE
#                 print(generated_name)
#                 with open(f'../image/{generated_name + filename}', 'wb') as f:
#                     for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
#                         print('Received a Chunk')  # DEBUG
#                         f.write(chunk)
#             else:
#                 with open(f'../image/{filename}', 'wb') as f:
#                     for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kilobytes
#                         print('Received a Chunk')  # DEBUG
#                         f.write(chunk)
#         elif behavior == 3:  # BREAK , COZ FILE IS IN THE DIRECTORY
#             print(f'This file is in directory.')
#     if method == 2:  # FULL SIZE FILE DOWNLOAD METHOD
#         if behavior == 1:
#             pass
#         elif behavior == 2:
#             pass
#         elif behavior == 3:
#             pass
#     else:
#         pass

#  Binary Download

# image = requests.get('url')
# with open('file_name', 'wb') as f:
#     f.write(image.content)
#
# #  Chunk download
# req = requests.get('url', stream=True)
#
# with open('filename.jpg', 'type') as f:
#     for chunk in req.iter_content(chunk_size=50000):  # 50000 = 50 kbytes
#         print('Received a Chunk')
#         f.write(chunk)

# download(
# 'https://images.unsplash.com/photo-1614245062871-a28dd5b7566b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D'
# '&ixlib=rb-1.2.1&auto=format&fit=crop&w=2134&q=80')

# download_image('https://cdn.pixabay.com/photo/2021/02/16/10/53/girl-6020659_960_720.jpg', 1, 2)

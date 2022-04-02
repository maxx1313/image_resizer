from PIL import Image
import pathlib
from termcolor import colored


intro = colored("""                   
                            **** IMAGE RESIZER v1.2 ****
                              Welcome to Image Resizer


Change your image size to 1920px with a couple of easy steps

1. Enter the path of the image you want to resize.
2. Enter a path to the destination you want to save the image to, eg. /Users/yourname/Desktop/       
4. Enter the file name, it has to be the same file type as the image you are resizing, eg. image.jpg

""", 'blue')
print(intro)

image_file = input('Enter image path or drag in the image: ')
image_file_extension = pathlib.Path(image_file).suffix
error_text_file = colored('File type not supported. Try again...', 'red', attrs=['reverse'])
while not image_file.endswith(('.jpg', 'jpeg', '.png')):
    print(error_text_file)
    image_file = input('Enter image path or drag in the image: ')

save_to = input('Save to: ')
error_text_save_to = colored("""Path needs to end with "/" Try again...""", 'red', attrs=['reverse'])
while not save_to.endswith('/'):
    print(error_text_save_to)
    save_to = input('Save to: ')

file_name = input('File_name: ')
file_name_extension = pathlib.Path(file_name).suffix
test = file_name_extension != image_file_extension
error_file_name = colored('The file extension has to be the same. Try again...', 'red', attrs=['reverse'])
while test:
    print(error_file_name)
    file_name = input('File_name: ')
    file_name_extension = pathlib.Path(file_name).suffix
    test = file_name_extension != image_file_extension

image = Image.open(image_file)
image.thumbnail((1920, 1920))
image.save(save_to + file_name)

print('Success! Image saved to: ' + save_to + file_name)
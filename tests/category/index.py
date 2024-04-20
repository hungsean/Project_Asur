from . import homepage
from function import image_process

def main(main_input_image):
    main_input_image = image_process.preprocess(main_input_image)

    # homepage
    homepage_index = homepage.check(main_input_image)

    response = ""
    for sub_index in homepage_index:
        response += str(sub_index) + "\n"

    return response
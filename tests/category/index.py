from . import homepage
from function import image_process

def main(main_input_image):
    main_input_image = image_process.preprocess(main_input_image)

    # homepage
    homepage_index = homepage.check(main_input_image)

    response = ""
    if homepage_index > 0.9:
        response = "homepage " + str(homepage_index)
    else:
        response = "unknown " + str(homepage_index)

    return response
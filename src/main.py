from function import image_process
from category import homepage

test_images = image_process.get_png_image("D:\\Programming\\Python\\20240408_Project_Asur\\Project_Asur\\assets\\screenshots\\")
for test_image in test_images:
    preprocess_test_image = image_process.image_preprocess(test_image)
    if preprocess_test_image.any() == None:
        continue
    homepage_similarity = homepage.check_homepage(preprocess_test_image)
    print("similarity: ", homepage_similarity)
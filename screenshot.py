from PIL import ImageGrab
from image import image_gray, image_binary, calculate_average_gray

coordinate = (353, 885, 1392, 1013)
coordinate_current = (1418, 885, 1497, 1013)


def card_shot():
    cards = []
    pic_left = ImageGrab.grab(coordinate)
    for num in range(13):
        region = (num * 80, 0, (num + 1) * 80, 129)
        crop_img = pic_left.crop(region)
        cards.append(crop_img)
    pic_right = ImageGrab.grab(coordinate_current)
    cards.append(pic_right)
    return cards

# gray = image_gray(pic)
#     resize_width = 16
#     resize_height = 26
#     smaller_image = gray.resize((resize_width, resize_height))
#     threshold = calculate_average_gray(gray, smaller_image)
#     binary = image_binary(smaller_image, threshold)
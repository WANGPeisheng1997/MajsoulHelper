from PIL import ImageGrab

# coordinate = (353, 885, 1393, 1014)
# coordinate_current = (1418, 885, 1498, 1014)
coordinate_left = (353, 892, 1473, 1007)
coordinate_right = (378, 892, 1498, 1007)


def card_shot():
    # shot for 28 slot
    cards = []
    pic_left = ImageGrab.grab(coordinate_left)
    pic_right = ImageGrab.grab(coordinate_right)
    for num in range(14):
        region = (num * 80, 0, (num + 1) * 80, 115)
        crop_img = pic_left.crop(region)
        cards.append(crop_img)

    for num in range(14):
        region = (num * 80, 0, (num + 1) * 80, 115)
        crop_img = pic_right.crop(region)
        cards.append(crop_img)
    return cards

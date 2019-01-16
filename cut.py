from PIL import Image
from image import crop_to_bin

img = Image.open('ui.png')
count = 0
card_name_dict = ["7s", "5p", "5s", "5z", "6m",
                  "6p", "6s", "6z", "7m", "7p",
                  "5m", "7z", "8m", "8p", "8s",
                  "9m", "9p", "9s", "", "2z",
                  "0p", "1s", "1z", "2m", "2p",
                  "0s", "2s", "3p", "3s", "3z",
                  "1m", "0m", "4m", "4s", "4z",
                  "1p", "3m", "4p", "", ""]


for x in range(0, 647, 81):
    for y in range(0, 649, 130):
        # x0 y0 x1 y1
        region = (x, y, x + 80, y + 129)
        crop_img = img.crop(region)
        card_name = card_name_dict[count]
        if card_name != "":
            crop_img.save("cards\%s.png" % str(card_name))
            binary_img = crop_to_bin(crop_img)
            binary_img.save("bin\%s.png" % str(card_name))
        count = count + 1

